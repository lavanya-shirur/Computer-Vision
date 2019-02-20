import cv2
from os import listdir
from os.path import isfile, join
import time
import os

finalcount = []
mypath="C:/Users/lavan/Desktop/cvproject/outputs/"
#mypath="C:/Users/lavan/Desktop/Project_trafficmgmt/data/"
#mypath="C:/Users/lavan/Desktop/Agradesem/Second-semester/Computer_vision/assignment3/cv_assignment/images_from_splitvideo/"
def detect(file):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print (timestr)
    IMAGE_FILE=mypath+file
    print (IMAGE_FILE)
    CASCADE_FILE = './cars.xml'
    #CASCADE_FILE = './lbpcascade.xml'
    CASCADE_ITEM = 'car'
    image = cv2.imread(IMAGE_FILE)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(CASCADE_FILE)
    #rectangles = cascade.detectMultiScale(gray, scaleFactor=1.1)
    rectangles = cascade.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=4,minSize=(20, 20))
                                          #,maxSize=(60,60))

    #rectangles = cascade.detectMultiScale(gray,scaleFactor=2)
    for (i, (x, y, w, h)) in enumerate(rectangles):
	    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
	    cv2.putText(image, CASCADE_ITEM + " #{}".format(i + 1), (x, y - 10),
		    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    #print("number of cars in this frame is ")
    #print(i+1)
    j=i+1
    finalcount.append(j)
    #print (finalcount)
    finalsum=(sum(finalcount))
    print (finalsum)

    if (finalsum<50):
        toll_rate=100
    else :
        toll_rate=200

    print ("the toll rate at this moment of time is")
    print (toll_rate)

    cv2.imshow(CASCADE_ITEM + "s", image)
    cv2.imwrite(timestr+".jpg",image)
    cv2.waitKey(1000)

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print ("files in list")
print (onlyfiles)
for m in range(len(onlyfiles)):
    a=detect(onlyfiles[m])
