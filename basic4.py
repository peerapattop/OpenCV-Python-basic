#กำหนดรูปแบบภาพ

import cv2 

img = cv2.imread("image/cat.jpg",-1) 
# 0 = รูปภาพสี Gray 
# 1 = รูปภาพสี 
# -1 = เติม chenel alpha 

imgresize = cv2.resize(img,(400,400)) 
cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows() 