import cv2
import numpy as np


def stCornerDetection(img):
    """
    Find the Shi - Tomasi Corner detector and mark them.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(img, (x,y), 3, 255, -1)
    return img
