import cv2
img=cv2.imread("image/shahinur.jpeg")
ImgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Imgblur=cv2.GaussianBlur(ImgGray,(99,99),0)
cv2.imshow("gray image",ImgGray)
cv2.imshow("orginal image",img)
cv2.imshow("image blur",Imgblur)
cv2.waitKey(0)