import numpy as np
import cv2

img=cv2.imread("img1.jpg",0)
print type(img), img.shape, type(int(img[307][0])) #f,c
s=img.tolist()
print s,type(s),len(s)
print type(img), img.shape, type(int(img[307][0])) #f,c
#print img.tolist()

#cv2.imshow("messi",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#f=open("dataImg",'w')
#f.write(int(s))
#f.close()

#print img
