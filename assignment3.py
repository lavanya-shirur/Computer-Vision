import os
import xml.etree.ElementTree as ET
import cv2

path = '/Users/lavan/Desktop/cv_assignment/PKLot/PKLot/parking1b/sunny'
for directory_sub, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".jpg"):
            countVal = 1
            img = cv2.imread(os.path.join(directory_sub, file))
            file1 = file.replace("jpg", 'xml')
            inputFile = open(os.path.join(directory_sub, file1), "r")
            XmlTree = ET.parse(inputFile.name)
            root = XmlTree.getroot()
            print(file1)
            for child in root:
                if (child.find('contour')) != None:
                    x = []
                    y = []
                    for child1 in child.iter('point'):
                        s = child1.get('x')
                        t = child1.get('y')
                        x.append(s)
                        y.append(t)
                    var1 = min(x)
                    var2 = max(x)
                    width = int(var2)-int(var1)
                    temp1 = min(y)
                    temp2 = max(y)
                    height = int(temp2)-int(temp1)

                    if child.get('occupied') == '1':
                        print("postive")
                        img1 = img[int(temp1):int(temp2), int(var1):int(var2)]
                        positive_val = "Positive/" + file.replace(".jpg", "")
                        negative_val = str(countVal) + ".jpg"
                        cv2.imwrite(positive_val + negative_val, img1)
                        param1 = "Positive/" + file.replace(".jpg", "")
                        param2 = str(countVal) + ".jpg"
                        img2 = cv2.imread(param1 + param2)
                        if img2 is not None:
                            line = "Positive/" + file.replace(".jpg", "") + str(countVal) + ".jpg" + ' 1 0 0 ' + str(width) + " " + str(height) + '\n'
                            # with open('info.lst', 'a') as f:
                            #     f.write(line)
                            file2 = open("info.lst", "a")
                            file2.write(line)
                            countVal = countVal + 1

                    elif child.get('occupied') == '0':
                        print("negative")
                        img1 = img[int(temp1):int(temp2), int(var1):int(var2)]
                        positive_val = "Negative/" + file.replace(".jpg", "")
                        negative_val = str(countVal) + ".jpg"
                        cv2.imwrite(positive_val + negative_val, img1)

                        line = "Negative/" + file.replace(".jpg", "") + str(countVal) + ".jpg" + '\n'
                        # with open('bg.txt', 'a') as f:
                        #     f.write(line)
                        file1 = open("bg.txt", "a")
                        file1.write(line)
                        countVal = countVal + 1

