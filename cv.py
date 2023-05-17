import torch
import cv2
import numpy as np
from kalmanfilter import KalmanFilter

#load model
model = torch.hub.load('.', 'custom', path='<where your model is>', source='local')
#capture video from camera
cap = cv2.VideoCapture(1)
#cameara setup
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FOURCC, 0x32595559)
cap.set(cv2.CAP_PROP_FPS, 120)
kf = KalmanFilter()
# cap = cv2.VideoCapture('')

while(True):
    ret, frame = cap.read()
    predict_x = 0
    predict_y = 0
    #img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY
    # B, G, R channel splitting
    #ret, thresh = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)
    # visualize the binary image
    img = frame;
    try:
        img = model(frame)
        x0 = img.pandas().xyxy[0].to_dict('records')[0].get("xmin")
        y0 = img.pandas().xyxy[0].to_dict('records')[0].get("ymin")
        x1 = img.pandas().xyxy[0].to_dict('records')[0].get("xmax")
        y1 = img.pandas().xyxy[0].to_dict('records')[0].get("ymax")
        x_cen,y_cen = int((x0+x1)/2),int((y0+y1)/2)
        print(x_cen,y_cen)
        predict_x, predict_y = kf.predict(x_cen,y_cen)
    except:
        pass
    out_img = np.squeeze(img.render())
    cv2.circle(out_img, (predict_x,predict_y), 20, (0, 0, 255), -1)
    cv2.imshow('YOLO', out_img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()