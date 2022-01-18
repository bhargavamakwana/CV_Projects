import cv2


def render(inp):
    """
    render frames based on input. It can be image or an video.
    """
    def video_render(inp):
        # read camera/video input
        cap = cv2.VideoCapture(inp)
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Cannot receive frame! Exiting...")
                break
            yield frame
    image_formats = ['jpg', 'png']
    form = inp.split(".")[-1]
    if form != "" and form not in image_formats:
        return video_render(inp)
    img = cv2.imread(inp)
    return img
