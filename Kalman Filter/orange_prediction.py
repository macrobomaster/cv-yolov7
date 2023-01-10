#https://pysource.com/2021/10/29/kalman-filter-predict-the-trajectory-of-an-object/
import cv2
from orange_detector import OrangeDetector
from kalmanfilter import KalmanFilter

cap = cv2.VideoCapture("orange.mp4")

#load detector
od = OrangeDetector()

#load kalmanFilter
kf = KalmanFilter()

while True:
    ret, frame = cap.read()

    #check if there is a frame or not
    if ret is False:
        break

    #location of the orange located
    orange_bbox = od.detect(frame)
    x,y,x2,y2 = orange_bbox
    cx = int((x+x2)/2)
    cy = int((y+y2)/2)
    predicted = kf.predict(cx,cy)

    cv2.circle(frame,(cx,cy),20, (0,0,255),-1)
    cv2.circle(frame, (predicted[0], predicted[1]), 20, (0, 255, 0), 4)
    #cv2.rectangle(frame, (x,y),(x2,y2),(255,0,0),4)
    cv2.imshow("frame",frame)
    key = cv2.waitKey(100)


    if key == ord('q'):
        break