import cv2
import numpy as np
from argument_utils import argument_parser
from stc import stCornerDetction

args = argument_parser()


img = cv2.imread(args.path)
img = cv2.resize(img, (960, 720))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# resize doesn't take the third dimension
# W H C
# Harris Corner detection
"""
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow("out", img)
cv2.waitKey(0)
"""


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(frame, (x,y), 3, 255, -1)
    cv2.imshow("out", frame)
    if cv2.waitKey(1) == ord('q'):
        break


# Shi Tomasi Corner Detection.

img = stCornerDetection(img)
cv2.imshow("out", img)
cv2.waitKey(0)
