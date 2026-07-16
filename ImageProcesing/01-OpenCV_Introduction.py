import cv2
#pip3 install opencv-python
img = cv2.imread('img_42.jpg')
#cv2.imshow('result',img)
#print(img)
# BLACK N WHITE
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#img, (x,y), (w,h), (color), borderWidth
cv2.rectangle(img,(20,20),(100,100),(255,0,0),5)
cv2.imshow('result',img)

# MISSING? - HAAR CASCASE CLASSIFIER XML FILE