import subprocess
import cv2


# Convert video from LOSSLESS AVI to MJPG or XVID
def convert_cv2(inPathName, outPathName, FOURCC='MJPG', crop=None):
    if (FOURCC != 'MJPG') and (FOURCC != 'XVID'):
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
    out = cv2.VideoWriter(outPathName,fourcc, fps, frameShape, isColor=False)

    print("Converting file", inPathName, "to", outPathName)
    print("total frames", nFrame, "shape", frameShape, "fps", fps)

    # Convert
    while True:
        ret, frame = capture.read()
        if ret:
            if crop is None:
                out.write(frame[:,:,0])
            else:
                out.write(frame[xmin:xmax,ymin:ymax,0])
        else:
            break


    # Release everything if job is finished
    out.release()
    
    
def convert_ffmpeg_h265(src_name, trg_name, lossless=False, crf=22, gray=False, crop=None):
    print("aaaaaaaaaaaaaa")
    
    task = ["ffmpeg","-i", src_name]
    
    # Determine color
    if gray:
        task += ["-vf", "format=gray"]
        
    # Crop if necessary
    if crop is not None:
        xmin, xmax, ymin, ymax = crop
        out_w = xmax - xmin
        out_h = ymax - ymin
        task += ["-vf", "crop="+str(out_w)+":"+str(out_h)+":"+str(xmin)+":"+str(xmax)] #"--filter:v"
    
    # VCodec
    task += ["-c:v", "libx265"]
    
    # Determine quality
    if lossless:
        task += ["-x265-params", "lossless=1"]
    else:
        task += ["-preset", "slow", "-x265-params", "crf=22"]
        
    # Target must appear at the end of the task
    task += [trg_name]
    
    # Run
    subprocess.run(task)