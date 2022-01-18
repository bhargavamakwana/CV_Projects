import cv2
import numpy as np
from argument_utils import argument_parser



args = argument_parser()


# Extract SIFT feature. This feature is Scale invariant. As in it can detect
# corner for scaled and unscaled images too.



def SIFT_Extractor(inp):
    """
    find the extracted feature of the frame and add it to the original frame
    """
    # Check if the input type is a valid numpy array
    if type(inp) is not np.ndarray:
        raise Exception("The provided input is not a valid array. Please check!")
    gray = cv2.cvtColor(inp, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    kp = sift.detect(gray, None)

    inp = cv2.drawKeypoints(inp, kp, inp)
    return inp



cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    img = SIFT_Extractor(frame)
    cv2.imshow("out", frame)
    if cv2.waitKey(1) == ord('q'):
        break
img = cv2.imread(args.path)
# W H C
img = cv2.resize(img, (960, 720))
# Find SIFT features
img = SIFT_Extractor(img)

cv2.imshow("out", img)
cv2.waitKey(0)
