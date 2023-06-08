#การอัดวิดีโอ (Video Recorder)


import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') #เขียนวิดิโอเป็นนามสกุล XVID

result = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480)) #ชื่อวิดิโอ,รูปแบบ,จำนวนเฟมเรท,ขนาดวิดิโอ

while (cap.isOpened()): 

    check , frame = cap.read() 
    
    if check == True: 
        cv2.imshow("Output",frame)
        result.write(frame) #เขียนไฟล์ขึ้นมา
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else :
        break

result.release() #แสดงค่า
cap.release()
cv2.destroyAllWindows()