# Dependencies
# streamlink package must be installed.
# ffmpeg must be installed.

# Libraries
import cv2  # opencv-python package must be installed.
import sh # sh package must be installed.
import numpy
import json
import threading
import time

class DoubleBuffer:
    def __init__(self, width, height):
        self.writing = threading.Lock()
        self.cv = [threading.Condition(), threading.Condition()]
        self.available = [False, False]
        self.active_cell = 0
        self.buffers = numpy.empty((2, height, width, 3), dtype=numpy.uint8)

    def write(self, img):
        with self.writing:
            self.buffers[self.active_cell] = img
            with self.cv[self.active_cell]:
                self.available[self.active_cell] = True
                self.cv[self.active_cell].notify()
            print(str(self.active_cell), end="")

    def read(self):
        readfrom = self.active_cell
        with self.cv[self.active_cell]:
            while not self.available[self.active_cell]:
                print("Blocking")
                self.cv[self.active_cell].wait()
            self.available[self.active_cell] = False
        with self.writing:
            self.active_cell = (self.active_cell + 1) % 2
            print("")
        return numpy.copy(self.buffers[readfrom])

def get_resolution(url):
    streams = json.loads(str(sh.ffprobe(
        sh.streamlink([url, "best", "-O"], _piped=True, _ok_code=(0, 1)),
        ["-i", "-", "-v", "quiet", "-print_format", "json", "-show_streams"])))
    for s in streams['streams']:
        if s['codec_type'] == 'video':
            return s['width'], s['height']

def producer(url, db):
    w, h = get_resolution(url)
    for raw_image in sh.ffmpeg(
        sh.streamlink([url, "best", "-O"], _piped=True),
        ['-i', '-', '-f', 'image2pipe', '-pix_fmt', 'rgb24', '-vcodec', 'rawvideo', "-"],
        _out_bufsize=w * h * 3, _iter=True, _internal_bufsize=10):
        image = numpy.frombuffer(raw_image, dtype='uint8', count=w * h * 3)
        image = image.reshape((h, w, 3))
        db.write(image)

def consumer(db):
    for i in range(50):
        im = db.read()
        cv2.imshow('frame', im)
        time.sleep(3)

# Input: video url
url = "https://youtu.be/WPrH_ivypZ8" # Live Youtube

# Create buffer object.
db = DoubleBuffer(*(get_resolution(url)))
# Create and start video capturing thread
producer_t = threading.Thread(target=producer, args=(url, db))
producer_t.start()
# Show captured video
consumer(db)

# Release memory
cv2.destroyAllWindows()