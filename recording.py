import cv2
import time

# camera_id = "/dev/video0"
camera_id = 0
# cap = cv2.VideoCapture(camera_id, cv2.CAP_V4L2)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#
cap.set(cv2.CAP_PROP_FOURCC,fourcc) #cv2.VideoWriter_fourcc(*'mp4v')
cap.set(cv2.CAP_PROP_FPS, 90)

current_time = time.strftime("%Y%m%d-%H%M%S")
output = 'output_{}.mp4' .format(current_time)

out = cv2.VideoWriter(output, fourcc, 90, (1280, 720))

start_time = time.time()
frame_count =0
while(True):
    ret, frame = cap.read()
    if ret:
    #     frame_count+=1
        # Write the frame to the output file
        out.write(frame)
        print("recording")
    #
    #
    #     # Display the resulting frame
    #cv2.imshow('Frame', frame)
        # print(time.time())
        # If 5 seconds have passed, break the loop
        if time.time() - start_time > 10:
            break
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    else:
        break

print(frame_count/10)
# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()