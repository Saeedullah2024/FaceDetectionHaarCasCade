import cv2 as cv 

img = cv.imread('pictures/group.jpeg')
img = cv.resize(img , (600,400) , cv.INTER_LINEAR)
cv.imshow('Image' , img)

if img is None:
    print("Image is not loaded")

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

haar_Cascade = cv.CascadeClassifier('haar_face.xml')
face_react = haar_Cascade.detectMultiScale(gray , scaleFactor=1.1 , minNeighbors=1)
#Change minNeighbors accoridng to noise(Faces) in image (1 to 3)

for (x,y,w,h) in face_react:
    cv.rectangle(img , (x,y) , (x+w , y+h) , (0,255,0) , thickness=3)

cv.imshow('Deteced Image' , img)

cv.waitKey(0)
