import cv2
import numpy as np

def onChange(x):
    pass

path = "Resources/car_picture.png"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",24,179,onChange)
cv2.createTrackbar("Sat Min","TrackBars",17,255,onChange)
cv2.createTrackbar("Value Min","TrackBars",119,255,onChange)
cv2.createTrackbar("Hue Max","TrackBars",98,179,onChange)
cv2.createTrackbar("Sat Max","TrackBars",255,255,onChange)
cv2.createTrackbar("Value Max","TrackBars",255,255,onChange)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    v_min = cv2.getTrackbarPos("Value Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_max = cv2.getTrackbarPos("Value Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)      #각 픽셀에 대해 AND 연산, img1&2는 동일한 shape를 가져야함.

    cv2.imshow("Original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("MASK", mask)
    cv2.imshow("Result", imgResult)
    cv2.waitKey(1)
