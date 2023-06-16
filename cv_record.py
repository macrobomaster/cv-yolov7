import cv2
import time



camera_id = "/dev/video0"
cap = cv2.VideoCapture(camera_id, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cap.set(cv2.CAP_PROP_FPS, 120)

current_time = time.strftime("%Y%m%d-%H%M%S")
output = 'output_{}.mp4'.format(current_time)

out = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'MJPG'), 120.0, (640, 480))

start_time = time.time()

while(True):
    ret, frame = cap.read()
    if ret:
        # Write the frame to the output file
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # If 5 seconds have passed, break the loop
        if time.time() - start_time > 5:
            break
    else:
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()