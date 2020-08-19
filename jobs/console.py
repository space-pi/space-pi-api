from datetime import datetime
from picamera import PiCamera
import time

camera = PiCamera()
jobstarttime = time.time()

while True:
    now = datetime.now()
    startTime = now.replace(hour=5, minute=0, second=0, microsecond=0)
    endTime = now.replace(hour=23, minute=59, second=59, microsecond=0)
    if now > startTime and now < endTime:
        camera.capture('/home/pi/Public/picture' + now.strftime("%y%m%d%-H%M%S") + '.jpg')

    time.sleep(60.0 - ((time.time() - jobstarttime) % 60.0))
