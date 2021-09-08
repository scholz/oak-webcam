# oak-webcam
Use your oak (https://store.opencv.ai/products/oak-d) as webcam.

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

Note: cam will not show up in Windows 10 camera viewer but does work in browser and teams, etc.


# credits
* https://blog.ml6.eu/the-opencv-ai-kit-80215f4d1ba2
* https://docs.luxonis.com/projects/api/en/latest/samples/rgb_preview/
