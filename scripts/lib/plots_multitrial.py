import os
import h5py
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import copy

from IPython.display import display

from lib.qt_wrapper import gui_fname, gui_fnames, gui_fpath
from lib.constraints import compute_constraints
from lib.stickman import stickman

class SessionPostprocess:

    def __init__(self, fnameH5, fnameTemplate, fpathVideo, fpathResult):
        self.fnameH5 = fnameH5
        self.fnameTemplate = fnameTemplate
        self.fpathResult = fpathResult
        self.fpathVideo = fpathVideo
        self.sessionName = os.path.basename(os.path.dirname(self.fnameH5))

        # Parse JSON file
        with open(self.fnameTemplate) as json_file:
            self.templateParam = json.load(json_file)

        # Read metadata from tracking file
        with h5py.File(self.fnameH5, "r") as h5file:
            # self.nodeNames = np.array(h5file['nodeNames'])
            self.nodeNames = np.array(h5file['NODE_NAMES'])
            self.nTimesMax, self.nNodes, self.nTrials = h5file['X'].shape
            self.fps = float(np.array(h5file['FPS']))
            self.vidPath = np.string_(h5file.attrs['VID_PATH']).decode()
            self.timesArr = np.arange(self.nTimesMax) / self.fps
            self.nTimesPerTrial = np.sum(1 - np.isnan(h5file['X'][:, 0, :]), axis=0)

    def display_trial_properties(self):
        print("Original path", self.vidPath)
        display(pd.DataFrame({
            "Framerate"                    : self.fps,
            "Maximal number of time steps" : self.nTimesMax,
            "Number of tracked nodes"      : self.nNodes,
            "Number of trials"             : self.nTrials
        }, index=(self.sessionName,)).T)

        # Determine video length
        plt.figure()
        plt.plot(self.nTimesPerTrial)
        plt.title("Number of frames per trial")
        plt.xlabel('Trial Index')
        plt.show()

    def display_quality_control(self, pThr):
        fig, ax = plt.subplots(nrows=self.nNodes, ncols=3, figsize=(15, 5*self.nNodes))
        fig2, ax2 = plt.subplots(ncols=2, figsize=(15, 5))

        with h5py.File(self.fnameH5, "r") as h5file:
            for iNode in range(self.nNodes):
                pErr = 1 - np.array(h5file['P'][:, iNode, :]).T
                pErrNoNan = np.copy(pErr)
                pErrNoNan[np.isnan(pErrNoNan)] = 1
                fErrTex = np.sum(pErrNoNan < pThr, axis=0) / np.sum(1 - np.isnan(pErr), axis=0)
                fErrTime = np.sum(pErrNoNan < pThr, axis=1) / np.sum(1 - np.isnan(pErr), axis=1)
                pErr[pErr == 0] = 1.0e-15

                ax[iNode][0].imshow(np.log10(pErr), vmin=-6, vmax=0, extent=[0, self.nTimesMax / self.fps, 0, self.nTrials], aspect='auto')
                ax[iNode][0].set_ylabel(self.nodeNames[iNode])
                # ax[iNode][0].get_xaxis().set_ticks([])
                ax[iNode][0].get_yaxis().set_ticks([])

                ax[iNode][1].plot(fErrTime)
                ax[iNode][2].plot(self.timesArr, fErrTex)
                ax[iNode][1].set_yticklabels(['{:,.1%}'.format(x) for x in ax[iNode][1].get_yticks()])
                ax[iNode][2].set_yticklabels(['{:,.1%}'.format(x) for x in ax[iNode][2].get_yticks()])

                ax2[0].plot(fErrTime, label=self.nodeNames[iNode])
                ax2[1].plot(self.timesArr, fErrTex, label=self.nodeNames[iNode])

                if iNode == 0:
                    ax[iNode][0].set_title("Log10(P[error]), (time x trial)")
                    ax[iNode][1].set_title("Freq(P[error]<0.01), by trial")
                    ax[iNode][2].set_title("Freq(P[error]<0.01), by timestep")

        ax[-1][0].set_xlabel("Time")
        ax[-1][1].set_xlabel("Trial Number")
        ax[-1][2].set_xlabel("Time")

        fig2.suptitle("Freq(P[error]<0.01)")
        ax2[0].set_xlabel("Trial Number")
        ax2[1].set_xlabel("Time")
        ax2[0].legend()
        ax2[1].legend()
        plt.show()

    def display_first_touch(self, pThr):
        with h5py.File(self.fnameH5, "r") as h5file:
            idxTouch = np.where(self.nodeNames == "Touch")[0][0]
            pErrTouch = 1 - np.array(h5file['P'][:, idxTouch, :]).T
            pErrTouch[np.isnan(pErrTouch)] = 1
            haveTouch = pErrTouch < pThr

        firstTouch = np.full(self.nTrials, np.nan)
        for iTrial in range(self.nTrials):
            candidates = np.where(haveTouch[iTrial])[0]
            if len(candidates) > 0:
                firstTouch[iTrial] = np.min(candidates)

        # Convert first touch from bin number to time
        firstTouch /= self.fps

        fig, ax = plt.subplots(nrows=2, figsize=(10, 10))
        ax[0].set_title("Estimated presence of touch")
        ax[1].set_title("Estimated first touch")
        ax[0].imshow(haveTouch, aspect='auto', extent=[0, self.nTimesMax / self.fps, 0, self.nTrials])
        ax[1].plot(firstTouch)
        plt.show()

    def _test_vid_exists(self, fpathname, extLst):
        for ext in extLst:
            rezPathName = os.path.splitext(fpathname)[0] + ext
            if os.path.isfile(rezPathName):
                print("Found file", os.path.basename(rezPathName))
                return rezPathName
            else:
                print("Not Found file", os.path.basename(rezPathName))

        raise IOError('No files for base have been found: ', fpathname)

    def write_stickman(self, trialIdx, showSummary=True):
        with h5py.File(self.fnameH5, "r") as h5file:
            filename = h5file['VID_NAMES'][trialIdx]
            x = np.copy(h5file['X'][:self.nTimesPerTrial[trialIdx], :, trialIdx])
            y = np.copy(h5file['Y'][:self.nTimesPerTrial[trialIdx], :, trialIdx])
            p = np.copy(h5file['P'][:self.nTimesPerTrial[trialIdx], :, trialIdx])

        constr_dict = compute_constraints(x, y, p, self.templateParam)
        if showSummary:
            display(constr_dict["summary"])

        paramThisTrial = copy.deepcopy(self.templateParam)
        vidPathName = os.path.join(self.fpathVideo, filename)

        paramThisTrial['SOURCE_PATH_NAME'] = self._test_vid_exists(vidPathName, ['.avi', '.mp4'])
        paramThisTrial['REZ_FPATH'] = self.fpathResult
        # paramThisTrial['AVI_FNAME'] = "/media/aleksejs/My Book/whisk_data/mtp_13/mtp_13_2017_03_09_a/2017_03_09_14_54_16.avi"

        stickman(x, y, paramThisTrial, constr_dict)  # , fps=FPS)