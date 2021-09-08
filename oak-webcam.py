# uses the preview stream for more flexible resolutions on oak
import cv2
import depthai as dai
import pyvirtualcam
from pyvirtualcam import PixelFormat

# Create pipeline
pipeline = dai.Pipeline()

# Define source and output
camRgb = pipeline.createColorCamera()
xoutVideo = pipeline.createXLinkOut()
xoutVideo.setStreamName("video")

# settings
width = 800
height = 600
fps = 20 

# preview output using opencv imshow
preview = False

# print fps on virtual camera
print_fps = False

# Properties
camRgb.setPreviewSize(width, height)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)
camRgb.setFps(fps)

xoutVideo.input.setBlocking(False)
xoutVideo.input.setQueueSize(1)

# Linking to preview stream
camRgb.preview.link(xoutVideo.input)

# Connect to device and start pipeline
with dai.Device(pipeline) as device:

    video = device.getOutputQueue(name="video", maxSize=1, blocking=False)
    
    with pyvirtualcam.Camera(width, height, fps, fmt=PixelFormat.BGR, print_fps=True) as cam:
        print(f'Virtual cam started: {cam.device} ({cam.width}x{cam.height} @ {cam.fps}fps)')

        while True:
            videoIn = video.get()
            # Get BGR frame from NV12 encoded video frame to show with opencv
            frame = videoIn.getCvFrame()

            if preview:
                # Visualizing the frame on slower hosts might have overhead
                cv2.imshow("video", frame )
            
            # Send to virtual cam.
            cam.send(frame)

            if cv2.waitKey(1) == ord('q'):
                break






    