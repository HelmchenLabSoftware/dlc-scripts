'''
Stickman V1.01
  - ARGV[1] : Gets DLC CSV file with coordinates of 5 joints
  - Computes distances between joints, as well as velocity of each joint
  - Marks joints as bad if their velocity exceeds 70pix / frame
  - Marks distances as bad if they exceed [0.5x, 2.0x] scale of their mean value
  - Report number of bad joints and distances
  - Save video of joints and distances.
    - Change color of joint circle if it is predicted to be bad in this frame
    - Change color of distance line if it is predicted to be bad in this frame

TODO-EXTENSIONS:
  [+] Predict number of nodes, their x,y,p from header
  [+] Enable edge shape template from file
  [+] Study likelihood value p, mark some joints as missing if p too small.
  [+] Enable half-complete limbs in case of missing joints. See if any are actually missing
  [ ] Experiment with threshold. See if there are advices from DLC people
  [ ] Optionally - allow automatic save of all (supposedly) bad frames as images
  [ ] Add angles as a metric. Specify ranges for angles in the file
    [ ] Include virtual joint, ask Pia
  [ ] Consider removing velocity as a test - it does not appear to offer anything more than length already offers
    [+] If keep velocity - fix bug where it always marks one more point than is actually necessary
    [ ] Still some bug - not worth effort
  [ ] Ultimate statistics - plot ratio of (bad length frames / all kept frames) as function of cutoff threshold. Thus optimize threshold
  
  [ ] Optionally - enable original video overlay
  [ ] Compare with HDF5 file they save
'''

import os
import numpy as np
import cv2

from lib.video_convert_lib import convert_ffmpeg_h265
from lib.color_lib import rainbow


def stickman(X, Y, param, constr_dict):

    ############################################
    # Extract video properties from original
    ############################################
    if not os.path.isfile(param["SOURCE_PATH_NAME"]):
        raise IOError("The video file does not exist", param["SOURCE_PATH_NAME"])
        
    capture = cv2.VideoCapture(param["SOURCE_PATH_NAME"])
    fps = cv2.CAP_PROP_FPS
    frameShape = (
        int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), 
        int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    
    ############################################
    # Define Constants
    ############################################

    FRAME_X_LIM = param["STICKMAN_CROP_X"] if "STICKMAN_CROP_X" in param.keys() else [0, frameShape[0]]
    FRAME_Y_LIM = param["STICKMAN_CROP_Y"] if "STICKMAN_CROP_Y" in param.keys() else [0, frameShape[1]]

    pointLocalCoord = lambda iFrame, iNode: (
        int(X[iFrame, iNode] - FRAME_X_LIM[0]),
        int(Y[iFrame, iNode] - FRAME_Y_LIM[0]))

    nRows, nNodes = X.shape

    CIRCLE_THICKNESS = -1  # Filled circle
    CIRCLE_RADIUS = 5
    EDGE_THICKNESS = 2

    COLOR_RED = (255, 0, 0)
    COLOR_GREEN = (0, 255, 0)
    COLOR_BLUE = (0, 0, 255)

    nodeColors = (rainbow(nNodes) * 255).astype(np.uint8)
    nodeColors = nodeColors[:, (0,2,1)]  # CV strange color order
    nodeColors = [tuple([int(c[0]), int(c[1]), int(c[2])]) for c in nodeColors]  # OpenCV is a princess wrt data types
    
    ############################################
    # Check constraints
    ############################################
    # Use velocity as node constraint for stickman plot.
    nodeLowConf = constr_dict["nodeLowConf"]
    haveNodeConstr = param["HAVE_V_CONSTR"]
    if haveNodeConstr:
        nodeLowConstr = np.copy(constr_dict["nodeBadV1"])
        
    # Use edge length as edge constraint for stickman plot
    haveEdges      = "EDGE_NODES" in param.keys()
    haveEdgeConstr = param['HAVE_EDGE_CONSTR']
    if haveEdges:
        edgeLowConf = constr_dict["edgeLowConf"]
    if haveEdgeConstr:
        edgeLowConstr = np.copy(constr_dict["edgeBadLength"])


    ###############
    #  Plot video
    ###############

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')

    basename = os.path.splitext(os.path.basename(param["SOURCE_PATH_NAME"]))[0]
    outName = os.path.join(param["REZ_FPATH"], basename + "-stickman.avi")
    outWriter = cv2.VideoWriter(outName, fourcc, fps, frameShape, isColor=True)

    for iFrame in range(nRows):
        print("Writing video ["+str(iFrame+1)+'/'+str(nRows)+']\r', end="")

        # Note CV2 column-major
        if param["STICKMAN_OVERLAY"]:
            success, pic = capture.read()
        else:
            pic = np.zeros((frameShape[1], frameShape[0], 3), dtype=np.uint8)
        
        
        # ------------Draw Edges----------------
        # If Edge has high confidence, draw it
        # Change color if edge has bad length
        if haveEdges:
            nEdges = len(param['EDGE_NODES'])
            for iEdge in range(nEdges):
                p1idx, p2idx = param['EDGE_NODES'][iEdge]

                if not edgeLowConf[iFrame, iEdge]:
                    p1 = pointLocalCoord(iFrame, p1idx)
                    p2 = pointLocalCoord(iFrame, p2idx)
                    badEdge = haveEdgeConstr and edgeLowConstr[iFrame, iEdge]
                    color = COLOR_RED if badEdge else COLOR_GREEN
                    pic = cv2.line(pic, p1, p2, color, EDGE_THICKNESS)

        # ------------Draw Nodes----------------
        # If Node has high confidence, draw it
        # Change color if node has bad velocity
        for iNode in range(nNodes):
            if not nodeLowConf[iFrame, iNode]:
                p1 = pointLocalCoord(iFrame, iNode)
                badNode = haveNodeConstr and nodeLowConstr[iFrame, iNode]
                # color = COLOR_RED if badNode else COLOR_BLUE
                # pic = cv2.circle(pic, p1, CIRCLE_RADIUS, color, CIRCLE_THICKNESS)

                if not badNode:
                    pic = cv2.circle(pic, p1, CIRCLE_RADIUS, nodeColors[iNode], CIRCLE_THICKNESS)
                else:
                    p1neg = p1[0] - CIRCLE_RADIUS, p1[1] - CIRCLE_RADIUS
                    p1pos = p1[0] + CIRCLE_RADIUS, p1[1] + CIRCLE_RADIUS
                    pic = cv2.rectangle(pic, p1neg, p1pos, nodeColors[iNode], CIRCLE_THICKNESS)

        outWriter.write(pic)#frame.transpose())  # OPENCV is col-major :(

        # cv2.imshow("cool", pic)
        # cv2.waitKey(0)
        # plt.figure()
        # plt.imshow(pic/255)
        # plt.show()

    # Release everything if job is finished
    capture.release()
    outWriter.release()
    cv2.destroyAllWindows()

    print("\nDone writing!")

    print("Compressing to MP4")
    outNameMP4 = os.path.splitext(outName)[0] + ".mp4"
    convert_ffmpeg_h265(outName, outNameMP4)
    print("Deleting uncompressed")
    os.remove(outName)
