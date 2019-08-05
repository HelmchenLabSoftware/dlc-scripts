import numpy as np
# import pandas as pd
from collections import OrderedDict, defaultdict
import cv2

from lib.os_lib import getfiles_walk
from lib.hdf5_wrapper import npStrArr2h5


def parse_dlc_csv(fname):
    # Read file
    with open(fname, 'r') as f:
        lines = f.readlines()

    # Parse CSV data
    nodeNames = list(OrderedDict.fromkeys(lines[1].strip().split(',')[1:]))
    data = np.array([line.strip().split(',') for line in lines[3:]]).astype(float)
    # df = pd.read_csv(dataFileName, sep=',', header=None, dtype=float, skiprows=3)
    # print("Data shape is", data.shape)
    nNodes = len(nodeNames)
    # nRows = data.shape[0]

    # Extract column positions from header
    bodyparts = np.array(lines[1].strip().split(','))
    properties = np.array(lines[2].strip().split(','))
    colX = np.zeros(nNodes, dtype=int)
    colY = np.zeros(nNodes, dtype=int)
    colP = np.zeros(nNodes, dtype=int)
    for i in range(nNodes):
        thiscols = bodyparts == nodeNames[i]
        colX[i] = np.where(np.logical_and(thiscols, properties == 'x'))[0]
        colY[i] = np.where(np.logical_and(thiscols, properties == 'y'))[0]
        colP[i] = np.where(np.logical_and(thiscols, properties == 'likelihood'))[0]
        
    return nodeNames, data[:, colX], data[:, colY], data[:, colP]


# Get fps of the video
def parse_avi_meta(vidname):
    with cv2.VideoCapture(vidname) as capture:
        fps = capture.get(cv2.CAP_PROP_FPS)
    return fps


'''
1. Crawl from root, find all directories containing ['DeepCut_resnet50', '.csv']
2. For each directory, compress all files into one sub file with same name as directory
'''
def dlc_csv_composite_crawl(rootdir, outdir):
    
    # Construct dictionary of files indexed by the containing folder name
    def paths2dict(walkpaths):            
        path_dict = defaultdict(list)
        for path, name in walkpaths:
            path_dict[os.path.basename(path)] += [os.path.join(path, name)]
        return path_dict
    
    walkpaths_csv = getfiles_walk(rootdir, ['DeepCut_resnet50', '.csv'])
    walkpaths_avi = getfiles_walk(rootdir, ['.avi'])
    
    path_dict_csv = paths2dict(walkpaths_csv)
    path_dict_avi = paths2dict(walkpaths_avi)
        
    # For each folder, create an output file that merges files inside
    for basename, csv_path_list in path_dict.items():
        assert basename in path_dict_avi.keys(), basename + " has .csv but no videos"        
        dlc_csv_merge_write(csv_path_list, path_dict_avi[basename], basename+'.h5')

        
'''
1. Read all files
  1.1 Number of AVI and CSV files must match
  1.2 All nodeNames must match
  1.3 All framerates must match
2. Determine longest nTime, make outArray [nTimesMax, nNodes, nTrials] of np.nan
3. Fill array with data
4. Save to H5
'''
def dlc_csv_merge_write(csv_list, vid_list, outname):
    # Check if all elements of a list are the same
    def check_equal(lst, err=""):
        for el in lst[1:]:
            if el != lst[0]:
                raise ValueError(err, lst[0], "!=", el)
    
    if len(csv_list) != len(vid_list):
        raise ValueError("There are", len(vid_list), "videos and", len(fpath), " csv files")
    
    # Get data and fps
    csv_data_list = [parse_dlc_csv(fname) for fname in csv_list]
    avi_fps_list = [parse_avi_meta(vid_name) for vid_name in vid_list]
        
    # Assert that all framerates are the same
    # Assert that all nodeNames match exactly
    check_equal(avi_fps_list, err="Found non-matching framerates")
    check_equal([data[0] for data in csv_data_list], err="Found non-matching keys")
    
    # Determine nNodes, nTrials, and longest nTime
    nNodes   = len(alldata[0][0])
    nTrials  = len(flist)
    nTimesMax = np.max([data[1].shape[0] for data in csv_data_list])

    # Make output array
    outdata_X = np.full((nTimesMax, nNodes, nTrials), np.nan)
    outdata_Y = np.full((nTimesMax, nNodes, nTrials), np.nan)
    outdata_P = np.full((nTimesMax, nNodes, nTrials), np.nan)
    
    # Fill output array
    for i, (nodeNames, X, Y, P) in enumerate(csv_data_list):
        nTimesThis = X.shape[0]
        outdata_X[:nTimesThis, nNodes, :, i] = X
        outdata_Y[:nTimesThis, nNodes, :, i] = Y
        outdata_P[:nTimesThis, nNodes, :, i] = P
    
    # Write result to file
    print("Writing merged data of", nTrials, "videos to", outname)
    rezfile = h5py.File(outname, "w")
    npStrArr2h5(rezfile, csv_data_list[0][0], 'NODE_NAMES')
    npStrArr2h5(rezfile, csv_list, 'CSV_PATHS')
    npStrArr2h5(rezfile, vid_list, 'VID_PATHS')
    rezfile['X'] = outdata_X
    rezfile['Y'] = outdata_Y
    rezfile['P'] = outdata_P
    rezfile.close()