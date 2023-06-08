#วาดเส้นตรง (Draw Line/Arrow)

import cv2 

#อ่านภาพ
img = cv2.imread("image/cat.jpg")

#กำหนดขนาดภาพ
imgresize = cv2.resize(img,(700,700)) 


#line (ภาพ, จุดเริ่มต้าน (x,y) , จุดสุดท้าย (x,y) , สี (BGR) , ความหนา)
cv2.arrowedLine(imgresize,(100,100),(500,200),(255,0,0),5)
cv2.arrowedLine(imgresize,(20,0),(400,400),(0,255,0),5)

cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows() 