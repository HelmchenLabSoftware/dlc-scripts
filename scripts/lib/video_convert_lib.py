import os
import numpy as np
import subprocess
import cv2
import matplotlib.image as mpimg


# Convert codec from fourcc to string
def decode_fourcc(cc):
    return "".join([chr((int(cc) >> 8 * i) & 0xFF) for i in range(4)])


def get_info_cv2(inPathName):
    capture = cv2.VideoCapture(inPathName)
    return {
        'nFrame' : int(capture.get(cv2.CAP_PROP_FRAME_COUNT)),
        'fps'    : capture.get(cv2.CAP_PROP_FPS),
        'shape'  : (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))),
        'fourcc' : decode_fourcc(capture.get(cv2.CAP_PROP_FOURCC))
    }


def append_ext(pathName, ext):
    oldExt = os.path.splitext(pathName)[1]
    if oldExt == ext:
        return pathName
    elif oldExt == "":
        return pathName + '.' + ext
    else:
        raise ValueError('Attempting to set old extension', oldExt, 'to', ext)


def img_matplotlib_2_cv(img3D, isColor=False):
    # Make sure image is UINT8 and spans values [0, 255]
    img = np.uint8(img3D) if np.max(img3D) > 1 else np.uint8(255 * img3D)

    # Select correct color ordering, or only one color if grayscale
    colorReorder = np.array([2, 1, 0])  # OpenCV and Matplotlib seem to disagree about color order in RGB
    img = img[:, :, colorReorder] if isColor else img[:, :, 0]

    return img


# Convert video from LOSSLESS AVI to MJPG or XVID
def convert_cv2(inPathName, outPathName, FOURCC='MJPG', crop=None, isColor=False):
    if FOURCC not in ['MJPG', 'XVID']:
        raise ValueError("Unexpected target encoding", FOURCC)
    
    # Reader
    capture = cv2.VideoCapture(inPathName)
    nFrame = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = capture.get(cv2.CAP_PROP_FPS)
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    if crop is not None:
        xmin, xmax, ymin, ymax = crop
        width = xmax - xmin
        height = ymax - ymin

    # Writer
    frameShape = (width, height)
    fourcc = cv2.VideoWriter_fourcc(*FOURCC)
    outPathNameEff = append_ext(outPathName, 'avi')
    out = cv2.VideoWriter(outPathNameEff, fourcc, fps, frameShape, isColor=isColor)

    print("Converting file", inPathName, "to", outPathName)
    print("total frames", nFrame, "shape", frameShape, "fps", fps)

    # Convert
    while True:
        ret, frame = capture.read()
        if ret:
            if crop is not None:
                frame = frame[xmin:xmax,ymin:ymax]

            if not isColor:
                frame = frame[:,:,0]

            out.write(frame)
        else:
            break


    # Release everything if job is finished
    out.release()
    

# Convert video from any AVI to any other
def convert_ffmpeg_h265(srcName, trgName, lossless=False, crf=22, gray=False, crop=None):
    trgNameEff = append_ext(trgName, 'mp4')

    task = ["ffmpeg","-i", srcName]
    
    # Determine color
    if gray:
        task += ["-vf", "format=gray"]
        
    # Crop if necessary
    if crop is not None:
        xmin, xmax, ymin, ymax = crop
        out_w = xmax - xmin
        out_h = ymax - ymin
        task += ["-vf", "crop="+str(out_w)+":"+str(out_h)+":"+str(xmin)+":"+str(ymin)] #"--filter:v"
    
    # VCodec
    task += ["-c:v", "libx265"]
    
    # Determine quality
    if lossless:
        task += ["-x265-params", "lossless=1"]
    else:
        task += ["-preset", "slow", "-x265-params", "crf=22"]
        
    # Target must appear at the end of the task
    task += [trgNameEff]
    
    # Run
    subprocess.run(task)


# Convert a set of images to a video
def merge_images_cv2(srcPaths, trgPathName, fps=30, FOURCC='MJPG', isColor=False):
    print("Writing video to", trgPathName)

    if FOURCC not in ['MJPG', 'XVID']:
        raise ValueError("Unexpected target encoding", FOURCC)

    # Load 1 picture to get its shape
    img = mpimg.imread(srcPaths[0])

    # Convert between standards of different libraries
    shape2Dcv = (img.shape[1], img.shape[0])   # OpenCV uses column-major or sth

    # Initialize writer
    fourcc = cv2.VideoWriter_fourcc(*FOURCC)
    outPathNameEff = append_ext(trgPathName, 'avi')
    out = cv2.VideoWriter(outPathNameEff, fourcc, fps, shape2Dcv, isColor=isColor)

    for iSrc, srcPath in enumerate(srcPaths):
        print('Processing image[%d]\r' % iSrc, end="")
        imgSrc = mpimg.imread(srcPath)
        imgSrc = img_matplotlib_2_cv(imgSrc, isColor=isColor)

        out.write(imgSrc)

    print("\n Done")

    out.release()


def save_frames_cv2(vidPath, outpath, frameIdxs, prefix='img'):

    def _add_leading_zeros(num, nDigit):
        s = str(num)
        l = len(s)
        if l < nDigit:
            s = "0"*(nDigit - l) + s
        return s

    capture = cv2.VideoCapture(vidPath)

    for idx in frameIdxs:
        capture.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = capture.read()

        outname = os.path.join(outpath, prefix + _add_leading_zeros(idx, 4) + '.png')
        cv2.imwrite(outname, frame)