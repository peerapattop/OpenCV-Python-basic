#เปิดกล้องด้วย OpenCV

import cv2

cap = cv2.VideoCapture(0) #  0 คือ ระบุหมายเลขกล้อง 

while (True):
    check , frame = cap.read() #รับภาพจากล้อง frame ต่อ frame 
    #อ่านค่าได้จะเป็น True ไม่ได้เป็น False
    #ถ้าตัวแปร check เป็นจริงจะได้ภาพ
    cv2.imshow("Output",frame)

    if cv2.waitKey(1) & 0xFF == ord("e") : #รอรับ key ถ้ากด e จะหลุดออกจาก loop while
        break

cap.release()
cv2.destroyAllWindows()