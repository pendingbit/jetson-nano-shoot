import cv2
from threading import Thread
from time import sleep
import argparse
from trigger import Trigger_GetFlag,Trigger_ClearFlag,Trigger_Task

dispW=640
dispH=480
photocount = 0
window_title="Shoot Screen"
camSet =f"v4l2src device=/dev/video0 io-mode=2 " \
    f"! image/jpeg, width={dispW}, height={dispH}, framerate=30/1, format=MJPG " \
    f"! nvv4l2decoder mjpeg=1 " \
    f"! nvvidconv " \
    f"! video/x-raw, format=BGRx " \
    f"! videoconvert " \
    f"! video/x-raw, format=BGR " \
    f"! appsink drop=1"

def shoot_task():
    global cam
    global photocount

    while True:
        #read frame from webCam 
        ret, frame = cam.read()
        
        #show oritnal cam
        cv2.imshow(window_title, frame)

        if Trigger_GetFlag() == True:
            print("shooting")
            photocount+=1
            cv2.imwrite(logpath+str(photocount)+".jpg", frame)
            Trigger_ClearFlag()

        if cv2.waitKey(1)==ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
   

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='指定保存照片及日志的路径')
    parser.add_argument('logpath', type=str,help='指定路径路径')
    args = parser.parse_args()
    logpath = args.logpath
    print("save path is ", logpath)

    print(cv2.__version__)
    cam=cv2.VideoCapture(camSet, cv2.CAP_GSTREAMER)
    cv2.namedWindow(window_title,cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(window_title, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

    triggerthread = Thread(target = Trigger_Task)
    triggerthread.daemon = True
    triggerthread.start()

    shoot_task()

