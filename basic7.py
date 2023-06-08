#เปิดวิดิโอด้วย OpenCV

#เปิดกล้องด้วย OpenCV

import cv2

cap = cv2.VideoCapture("image/Video.mp4") #  0 คือ ระบุหมายเลขกล้อง 

while (True):
    check , frame = cap.read() 

    cv2.imshow("Output",frame)

    if cv2.waitKey(1) & 0xFF == ord("e") : #รอรับ key ถ้ากด e จะหลุดออกจาก loop while
        break

cap.release()
cv2.destroyAllWindows()