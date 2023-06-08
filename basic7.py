#เปิดวิดิโอด้วย OpenCV

import cv2

cap = cv2.VideoCapture("image/Video.mp4") #  ตำแหน่งวิดิโอ

while (cap.isOpened()): #เช็คว่าวิดิโอว่าทำงานได้หรือไม่

    check , frame = cap.read() 
    
    if check == True: #เช็คว่าค่าที่รับมายังมีอยู่หรือไม่ ถ้าใช้ให้ทำงาน
        cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"): #รอรับ key ถ้ากด e จะหลุดออกจาก loop while
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()