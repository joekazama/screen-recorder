# importing the required packages
import pyautogui
import cv2 #py -m pip install opencv-python
import numpy as np
import time
from PIL import Image #pip install Pillow

# Specify resolution
print(pyautogui.size())
#resolution = tuple(pyautogui.size())
resolution = (700,700) # has to match cropped dimensions too 
  
# Specify video codec: DIVX: *'XVID'  MJPG: *'MJPG'
codec = cv2.VideoWriter_fourcc(*'XVID')

#capture webcam
# cap = cv2.VideoCapture(0)
  
# Specify name of Output file
T = str(time.time())
filename = T.replace(".", "-",1)
print("saved file: " , filename)
#filename = 'recorded' 

# Specify frames rate. We can choose any 
# value and experiment with it
fps = 10.0 
  
# Creating a VideoWriter object, MUST have .avi or won't save
out = cv2.VideoWriter(filename + ".avi", codec, fps, resolution)
  
# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
  
# Resize this window
cv2.resizeWindow("Live", 480, 270)

#img = pyautogui.screenshot('testing.jpg')
#region screenshot
#img = pyautogui.screenshot(filename + '.jpeg',region=(0,0, 300, 400))
#find an image onthe screen based off a supplied image, gives coordinates
#confidence level is to adjust accuracy
#button7location= pyautogui.locateOnScreen('calc7key.png', confidenc=0.9)
#center can be foud with .cent()
#pyautogui.center(button7location)

while True:
    # Take screenshot using PyAutoGUI
    #img = pyautogui.screenshot(region=(800,500, 640, 480))  #put screenshot name in screenshot() to save
    #won't record if there's a screenshot dimension mismatch or numpy mismatch
    img = pyautogui.screenshot()

    #CROP SCREENSHOT
    # define upper left and lower right corners (x,y,width, height)
    #imgcropped = img.crop(box = (0,0,800,600))
    #img = imgcropped
    #NEED TO USE NUMPY SLICING, not pyautogui crop
	#img[bottom:top, left:right]
	#cropped_img = img[y_start:y_end, x_start:x_end]

    # Convert the screenshot to a numpy array
    frame = np.array(img)
	
    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cropped = frame[200:900, 500:1200]  # [Y-start: Y-end , X-start: X-end]
    #Y =0 is top of screen.  
    #Has to be square dimensions!

    # Write it to the output file.  only accepts numpy arrays or scalars
    out.write(cropped) # write is expecting same size as when out was constructed
    #imageio.mimsave('C:\users\computer\desktop\' + filename, frame, fps=60)
      
    # Optional: Display the recording screen
    cv2.imshow('LIVE', cropped)
      
    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Release the Video writer
out.release()
  
# Destroy all windows
cv2.destroyAllWindows()