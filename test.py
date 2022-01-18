import cv2
from frame_renderer import render

inp = "bolt-detection.mp4"

imgs = render(inp)
for img in imgs:

    cv2.imshow("out", img)
    if cv2.waitKey(1) == ord('q'):
        break
