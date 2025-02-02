import cv2
#computer vision
import imutils
from cv2.data import haarcascades

print("OpenCV version : " + cv2.__version__)

img = cv2.imread("img.jpg") #Reading the image
bgr_img = cv2.cvtColor(img , cv2.COLOR_RGB2BGR) #RGB to BGR color format conversion
gray_img = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)
res_img = imutils.resize(img , height=200 , width=200)
gaussian_img = cv2.GaussianBlur(gray_img , (51,51) , 0)
threshold_img = cv2.threshold(gray_img , 150 , 255 , cv2.THRESH_BINARY)[1] #gray image conversion to binary image


#creating windows so that it can be resized later
cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.namedWindow('bgr', cv2.WINDOW_NORMAL)
cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
cv2.namedWindow('smoothen', cv2.WINDOW_NORMAL)
cv2.namedWindow('threshold', cv2.WINDOW_NORMAL)

#resizing windows
cv2.resizeWindow('original', 600, 400)
cv2.resizeWindow('bgr', 600, 400)
cv2.resizeWindow('gray', 600, 400)
cv2.resizeWindow('smoothen', 600, 400)
cv2.resizeWindow('threshold', 600, 400)

#printing image
cv2.imshow('original' , img)
cv2.imshow('bgr' , bgr_img)
cv2.imshow('gray' , gray_img)
cv2.imshow('resized img' , res_img)
cv2.imshow('smoothen' , gaussian_img)
cv2.imshow('threshold' , threshold_img)

#Saving an image
cv2.imwrite("bgr_img.jpg" , bgr_img)
cv2.imwrite("gray_img.jpg" , gray_img)
cv2.imwrite("resized_img.jpg" , res_img)
cv2.imwrite("blured_img.jpg" , gaussian_img)
cv2.imwrite("threshold_img.jpg" , threshold_img)

#waiting for user to close the windows , if not image would just vanish
cv2.waitKey(0)
cv2.destroyAllWindows() #close output

#finding contours in threshold img
contours, hierarchy = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#drawing contours on the original image
cv2.drawContours(img, contours, -1, (255, 0, 0), 5)

cv2.rectangle(img , (1,9) , (120,130) , (0,0,0) , 9)
cv2.putText(img , "Rectangle" , (50,50) , cv2.FONT_ITALIC , 3 , (0,0,255),3)
cv2.namedWindow('draw_rect', cv2.WINDOW_NORMAL)
cv2.resizeWindow('draw_rect', 600, 400)
cv2.imshow('draw_rect' , img)

cv2.waitKey(0)
cv2.destroyAllWindows()