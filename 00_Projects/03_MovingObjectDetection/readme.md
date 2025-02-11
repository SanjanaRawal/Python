# What is moving object detection?
Moving Object Detection is a technique used in computer vision and image processing. It is used to track objects that are in motion within the video or a sequence of images by detecting changes in position over time.  
 In it , multiple consecutive frames from a video are compared by various methods to determine if any moving object is detected.

# Key steps in moving object detection : 
1. Frame Differencing - Basic principle is to compare 2 consecutive frames. Motion is detected when there is a change in both the frames calculated by comparing difference in current and previous frame.
2. Background Subtraction - It is used to effectively isolate moving objects from the static background. It maybe simplified or may use advanced algorithms like Gaussian Mixture Models. Here , a simplified technique is used to subtract the background.
3. Thresholding - After detecting changes , threshold is applied to decide which differences are significant and needed to be considered. It helps to eliminate noise. 
4. Contour Detection - Once motion is detected , the system can now process the image to detect contours / boundaries of the object which is moving.
5. Tracking - Objects aren't tracked in the code right now , may update it afterward!

# Applications of moving object detection : 
1. Surveillance - To monitor security footage and detect unusual movements.
2. Autonomous Vehicles - To detect pedestrians , vehicles and obstacles on the road.
3. Smart Home Systems - Detecting motion in home security cameras , triggering alarms when movement is detected in restricted areas. 
4. Sports Analytics - Track players , balls etc. in live sports to provide insights , statistics , highlight plays.
5. WildLife Monitoring and Conservation - Monitor movements of animals in their natural habitat.

# Code explanation

1.Importing libraries 

import cv2  - Importing computer vision's , opencv library for image processing and computer vision related tasks 

import time  - For tasks needing time functions.  

import imutils - For image resizing 

2.Initializing Camera

cam = cv2.VideoCapture(0) - Using computer's primary (default) camera for capturing the video 

time.sleep(1) - Delay of one second 

3.Initializing Variables

firstFrame = None - Storing first frame of video for background subtraction , set none because nothing was captured initially 

area = 500 - Declaring a variable , which will be used to set a minimum contour area for object detection. Contour with area smaller than 500 will be ignored.

4.Frame Capturing Loop

while True: - an infinite loop 

    _, img = cam.read() - To read the image from cam , a variable that captures from the camera. Underscore is used because we only need captured image , which is returned as second value (img)
    if img is None: - When nothing is captured , programs prints the following stement 
        print("Failed to capture frame. Exiting...")
        break - And then exit the while loop in case no frame is found

INSIDE THE WHILE LOOP :-

5.Preprocessing the frame

text = "Normal" - variable declared which will be displayed on the image to indicate no movement is detected 

img = imutils.resize(img, width=800) - To resize the captured image with width of 800 pixels. It is used to speed up processing.

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) - Conversion of color format because gray images are easy to process and colors aren't required for movement detection.

gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0) - To apply gaussian blur to the image , it reduces noise , smoothens the image and hence motion detection becomes better

6.Setting first frame

 if firstFrame is None: -When first frame is none   
        firstFrame = gaussianImg -set firstFrame as gaussianImg  
        continue  - and continue i.e. skip rest of the loop and move to the next iteration , to ensure that first frame is used as reference background image


7.Calculate Frame Difference 

imgDiff = cv2.absdiff(firstFrame, gaussianImg)  - Calculates absolute difference between first/background image and current image , highlights the areas having a change

threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1] - Converts frame difference to binary image , for difference greater than threshold(25) white(255) is set and for less than threshold black(0) is set.

threshImg = cv2.dilate(threshImg, None, iterations=2) - Applying dilation helps to expand white areas i.e. where frame difference is large(region of motion) , helps to make movement easier to get detected.

8.Finding Contours 

cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) - To find contours , contours are used to represent continuous boundaries of objects

cnts = imutils.grab_contours(cnts) - To extract contours 

9.Processing each contour 

for c in cnts : - For every contour detected

INSIDE FOR LOOP - 

if cv2.contourArea(c) < area :  - if contour area of a contour is less than area i.e. 500 as set by us
continue 

(x, y, w, h) = cv2.boundingRect(c) - To calculate bounding box of the contour 

cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) - Draw a recatangle of particular RGB code of border 2 around moving object

text = "Moving Object Detected" - and update the text

10.Displaying image

cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) - Adds the previous/updated text to the image at mentioned position with red color

cv2.imshow("CameraFeed", img) - To display processed frame in a window whose title is CameraFeed

11.Loop Exiting Condition

key = cv2.waitKey(10) - wait to 10 seconds 
if key == ord("q") - when q key is pressed 
break - exit the while loop 

OUTSIDE THE WHILE LOOP - 

12.Close the window 

cam.release() - Releasing the camera so that it can be used by other applications 

cv2.destroyAllWindows() - Close all opencv windows that were opened during program execution 






















