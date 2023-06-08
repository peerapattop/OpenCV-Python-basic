#กำหนดขนาดภาพ (Resize)

import cv2 

img = cv2.imread("image/cat.jpg")
imgresize = cv2.resize(img,(400,400)) # ใช้ cv2.resize(ชื่อภาพ,(ขนาดภาพ,ขนาดภาพ))

cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows() 