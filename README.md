# oak-webcam
Use your OAK-D (https://store.opencv.ai/products/) as webcam and as cartoonizing webcam.
Tested this with:
* OAK-D-Lite (https://docs.luxonis.com/projects/hardware/en/latest/pages/DM9095.html)
* OAK-D (https://docs.luxonis.com/projects/hardware/en/latest/pages/BW1098OAK.html)

# instructions
In cmd.exe in windows navigate to git folder and run.

```cmd
python3.9 -m venv venv
venv\Scripts\activate.bat
pip -r requirements.txt
```

Follow instructions for installing a virtual camera interface:
https://github.com/letmaik/pyvirtualcam

Then run python oak-webcam.py and test the webcam eg.
using https://www.vidyard.com/cam-test/.

Note: cam will not show up in Windows 10 camera viewer but does work in browser and ms teams, etc.


# credits
* https://blog.ml6.eu/the-opencv-ai-kit-80215f4d1ba2
* https://docs.luxonis.com/projects/api/en/latest/samples/rgb_preview/
* https://github.com/PINTO0309/PINTO_model_zoo/tree/main/062_facial_cartoonization/01_float32
  * and more specifically
    *  https://github.com/yas-sim/DBFace-on-OpenVINO
    *  https://github.com/SystemErrorWang/FacialCartoonization.git
  
