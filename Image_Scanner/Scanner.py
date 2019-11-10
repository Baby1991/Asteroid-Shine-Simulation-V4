import cv2,os,numpy as np

path="C:\\Users\\Filip\\Desktop\\Asteroidi\\Sfera"
imageList=os.listdir(path)
i=imageList[0]
src =cv2.imread(os.path.join(path,i),cv2.IMREAD_GRAYSCALE)
ret, img = cv2.threshold(src, 2, 255, cv2.THRESH_BINARY) 

img=cv2.erode(img,np.ones((3,3)),iterations=20)
img=cv2.dilate(img,np.ones((3,3)),iterations=20)
new_image = src * ((img/255).astype(src.dtype))
cv2.imshow('rip',cv2.resize(new_image,(900,600)))
cv2.waitKey(0)
print(sum(sum(new_image)))




