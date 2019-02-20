import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('carcascade.xml')
print(face_cascade)

img = cv2.imread(r'C:/Users/lavan/Desktop/cv_assignment/PKLot/PKLot/parking1a/sunny/2012-12-11/2012-12-11_17_01_09.jpg')
#cv2.imshow("image",img)

cap= cv2.VideoCapture(0)
print (cap)
while 1:
    ret, img = cap.read()
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 20, 20)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()