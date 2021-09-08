# uses the preview stream for more flexible resolutions on oak
import cv2
import depthai as dai
import pyvirtualcam
from pyvirtualcam import PixelFormat
import numpy as np


# Create pipeline
pipeline = dai.Pipeline()
pipeline.setOpenVINOVersion(version=dai.OpenVINO.Version.VERSION_2021_3)

# settings
nn_shape = 256

# how much to increase actual output
scaling_factor = 3
fps = 20 


# Define camera stream
camRgb = pipeline.createColorCamera()
camRgb.initialControl.setManualFocus(130)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)
camRgb.setFps(fps)


# Define a neural network that will make predictions based on the source frames
detection_nn = pipeline.createNeuralNetwork()
detection_nn.setBlobPath("resources/nn/facial_cartoonization_256x256_openvino_2021.4_6shave.blob")
detection_nn.input.setBlocking(False)

# Link different inputs and outputs
# Send the resized 'preview' stream to the nn, while the high quality output is sent to another queue
camRgb.setPreviewSize(nn_shape, nn_shape)
camRgb.setInterleaved(False)
camRgb.preview.link(detection_nn.input)

# Create neural network output
detection_nn_xout = pipeline.createXLinkOut()
detection_nn_xout.setStreamName("nn")
detection_nn_xout.input.setBlocking(False)


# link with nn output
detection_nn.out.link(detection_nn_xout.input)

# preview output using opencv imshow
preview = True

# print fps on virtual camera
print_fps = False


# Connect to device and start pipeline
with dai.Device(pipeline.getOpenVINOVersion()) as device:

    device.startPipeline(pipeline)

    q_nn = device.getOutputQueue(name="nn", maxSize=1, blocking=False)
   
    
    with pyvirtualcam.Camera(nn_shape * scaling_factor, nn_shape * scaling_factor, fps, fmt=PixelFormat.BGR, print_fps=True) as cam:
        print(f'Virtual cam started: {cam.device} ({cam.width}x{cam.height} @ {cam.fps}fps)')

        while True:
            
            # get layer1 data
            in_nn = q_nn.tryGet()

            if in_nn is not None:
                
                layer1 = np.array(in_nn.getFirstLayerFp16()).reshape(3, nn_shape, nn_shape).transpose(1,2,0)
                layer1 = (layer1 +1) * 127.5
                frame = layer1.astype(np.uint8).copy()

                # Get BGR frame from NV12 encoded video frame to show with opencv
                if frame is not None:
                    
                    res = cv2.resize(frame ,None,fx=scaling_factor, fy=scaling_factor, interpolation = cv2.INTER_CUBIC)
                    if preview:
                        # Visualizing the frame on slower hosts might have overhead
                    
                        cv2.imshow("video", res )
                    
                    # Send to virtual cam.                    
                    cam.send(res)

                if cv2.waitKey(1) == ord('q'):
                    break






    