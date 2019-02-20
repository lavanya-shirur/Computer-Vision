import cv2
import argparse
import os
#print(cv2.__version__)

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True

    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*3000))    # added this line
      success,image = vidcap.read()
      print ('Read a new frame: ', success)
      #listimage=listimage.append(image)
      #print (listimage)
      count = count + 1
      carcount=pathOut+"\\frame"+ str(count)+".jpg"
      print (carcount)
      cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
      #length(pathOut)
    os.remove(carcount)

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    #print(args)
    extractImages(args.pathIn, args.pathOut)
