from django.shortcuts import render
import numpy as np
import threading
from django.http import StreamingHttpResponse
import cv2


"""
def capture_video_from_cam():
    cap = cv2.VideoCapture(0)
    currentFrame = 0
    while True:

        ret, frame = cap.read()

        # Handles the mirroring of the current frame
        frame = cv2.flip(frame,1)
        currentFrame += 1

def show_video_on_page(request):
    resp = StreamingHttpResponse(capture_video_from_cam())
    return render(request, 'base.html', {'video': resp})
 """
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

cam = VideoCamera()


def gen(camera):

    while True:
        frame = cam.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



def funopen(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass


# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def base(request):
    return render(request, 'blog/base.html', {})
