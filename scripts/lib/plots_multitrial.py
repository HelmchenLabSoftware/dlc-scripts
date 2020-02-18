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

    def __init__(self):
        self.param = {
            "H5_FNAME"      : gui_fname("Open DLC session results file", "./", "HDF5 files (*.h5)"),
            "TMP_FNAME"     : gui_fname("Select Postprocess Template Filename...", "./", "Template Files (*.json)"),
            "REZ_FPATH"     : gui_fpath("Select result path", "./")
        }

        # Parse JSON file
        with open(self.param["TMP_FNAME"]) as json_file:
            self.param.update(json.load(json_file))

        self.h5file = h5py.File(self.param["H5_FNAME"], "r")
        self.nodeNames = np.array(self.h5file['self.nodeNames'])
        self.nTimesMax, self.nNodes, self.nTrials = self.h5file['X'].shape
        self.fps = float(np.array(self.h5file['FPS']))
        self.vidPath = np.string_(self.h5file.attrs['VID_PATH']).decode()
        self.timesArr = np.arange(self.nTimesMax) / self.fps
        self.nTimesPerTrial = np.sum(1 - np.isnan(self.h5file['X'][:, 0, :]), axis=0)

    def display_trial_properties(self):
        print("Original path", self.vidPath)
        display(pd.DataFrame({
            "Framerate"                    : self.fps,
            "Maximal number of time steps" : self.nTimesMax,
            "Number of tracked nodes"      : self.nNodes,
            "Number of trials"             : self.nTrials
        }, index=(os.path.basename(self.h5path),)).T)

        # Determine video length
        plt.figure()
        plt.plot(self.nTimesPerTrial)
        plt.title("Number of frames per trial")
        plt.xlabel('Trial Index')
        plt.show()

    def display_quality_control(self, pThr):
        fig, ax = plt.subplots(nrows=self.nNodes, ncols=3, figsize=(15, 5*self.nNodes))
        fig2, ax2 = plt.subplots(ncols=2, figsize=(15, 5))
        for iNode in range(self.nNodes):
            pErr = 1 - np.array(self.h5file['P'][:, iNode, :]).T
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
        idxTouch = np.where(self.nodeNames == "Touch")[0][0]
        pErrTouch = 1 - np.array(self.h5file['P'][:, idxTouch, :]).T
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
        
    def write_stickman(self, trialIdx):
        x = self.h5file['X'][:self.nTimesPerTrial[trialIdx], :, trialIdx]
        y = self.h5file['Y'][:self.nTimesPerTrial[trialIdx], :, trialIdx]
        p = self.h5file['P'][:self.nTimesPerTrial[trialIdx], :, trialIdx]

        constr_dict = compute_constraints(x, y, p, self.param)
        display(constr_dict["summary"])

        paramThisTrial = copy.deepcopy(self.param)
        # # paramThisTrial['AVI_FNAME'] = os.path.join(VID_PATH, self.h5file['VID_NAMES'][trialIdx])
        # paramThisTrial['AVI_FNAME'] = "/media/aleksejs/My Book/whisk_data/mtp_13/mtp_13_2017_03_09_a/2017_03_09_14_54_16.avi"

        stickman(x, y, paramThisTrial, constr_dict)  # , fps=FPS)