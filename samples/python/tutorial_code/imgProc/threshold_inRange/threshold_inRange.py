# Forked from: https://docs.opencv.org/4.1.2/da/d97/tutorial_threshold_inRange.html

"""HSL (hue, saturation, lightness) or HSB (hue, saturation, brightness) 
and HSV (hue, saturation, value) are alternative representations of the RGB color model

Hue: is the color portion of the model, expressed as a number from 0 to 360 degrees:

    Red falls between 0 and 60 degrees.
    Yellow falls between 61 and 120 degrees.
    Green falls between 121 and 180 degrees.
    Cyan falls between 181 and 240 degrees.
    Blue falls between 241 and 300 degrees.
    Magenta falls between 301 and 360 degrees.

Saturation: Describes the amount of gray in a particular color, from 0 to 100 percent. 
Reducing this component toward zero introduces more gray and produces a faded effect. 
Sometimes, saturation appears as a range from 0 to 1, where 0 is gray, and 1 is a primary color.

Value (or Brightness): works in conjunction with saturation and describes the brightness or intensity
of the color, from 0 to 100 percent, where 0 is completely black, and 100 is the brightest 
and reveals the most color.
"""

from __future__ import print_function
import cv2 as cv
import argparse

max_value = 255
max_value_H = 360//2
low_H = 0
low_S = 0
low_V = 0
high_H = max_value_H
high_S = max_value
high_V = max_value
window_capture_name = 'Video Capture'
window_filter_name = 'Filter Mask'
window_result_name = 'Filtered Image'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'


def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H-1, low_H)
    cv.setTrackbarPos(low_H_name, window_filter_name, low_H)

def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H+1)
    cv.setTrackbarPos(high_H_name, window_filter_name, high_H)

def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S-1, low_S)
    cv.setTrackbarPos(low_S_name, window_filter_name, low_S)

def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S+1)
    cv.setTrackbarPos(high_S_name, window_filter_name, high_S)

def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V-1, low_V)
    cv.setTrackbarPos(low_V_name, window_filter_name, low_V)

def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V+1)
    cv.setTrackbarPos(high_V_name, window_filter_name, high_V)

parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
args = parser.parse_args()

## [cap]
cap = cv.VideoCapture(args.camera)
## [cap]

cv.namedWindow(window_capture_name)
cv.namedWindow(window_filter_name)
cv.namedWindow(window_result_name)

## [trackbar]
cv.createTrackbar(low_H_name, window_filter_name , low_H, max_value_H, on_low_H_thresh_trackbar)
cv.createTrackbar(high_H_name, window_filter_name , high_H, max_value_H, on_high_H_thresh_trackbar)
cv.createTrackbar(low_S_name, window_filter_name , low_S, max_value, on_low_S_thresh_trackbar)
cv.createTrackbar(high_S_name, window_filter_name , high_S, max_value, on_high_S_thresh_trackbar)
cv.createTrackbar(low_V_name, window_filter_name , low_V, max_value, on_low_V_thresh_trackbar)
cv.createTrackbar(high_V_name, window_filter_name , high_V, max_value, on_high_V_thresh_trackbar)


while True:
    ## [while]
    ret, frame = cap.read()
    if frame is None:
        break

    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    frame_filtered = cv.bitwise_and(frame, frame, mask=frame_threshold)
    ## [while]

    ## [show]
    cv.imshow(window_capture_name, frame)
    cv.imshow(window_filter_name, frame_threshold)
    cv.imshow(window_result_name, frame_filtered)
    
    ## [show]

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break

cv.destroyAllWindows()
cap.release()
