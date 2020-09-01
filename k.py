 
import picamera
# setup the camera such that it closes when done.
print ("About to take picture ")
with picamera.PiCamera() as camera:
     camera.resolution =(2592,1944)
     camera.capture("/home/pi/Desktop/robocpws/newimage.jpg")
print ("picture taken")
	 
