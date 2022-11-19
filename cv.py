import torch
import cv2
import numpy as np
#load model
model = torch.hub.load('.', 'custom', path='<where your model is>', source='local')
#capture video from camera
cap = cv2.VideoCapture(1)

# cap = cv2.VideoCapture('')

while(True):
    ret, frame = cap.read()
    
    #img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY
    # B, G, R channel splitting
    #ret, thresh = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)
    # visualize the binary image
    img = frame;
    try:
        img = model(frame)
    except:
        pass
    cv2.imshow('YOLO', np.squeeze(img.render()))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()