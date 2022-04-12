import cv2
faceCaseCade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while True:
    shahinur,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=faceCaseCade.detectMultiScale(img,1.1,4)
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
        cv2.imshow("img",img)
        k=cv2.waitKey(10) & 0xFF
        if k==27:
            break