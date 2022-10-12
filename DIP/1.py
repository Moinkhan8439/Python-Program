import cv2

img=cv2.imread("image-2017-10-05_1.png")
b,g,r=cv2.split(img)
cv2.namedWindow("red",cv2.WINDOW_NORMAL)
cv2.namedWindow("green",cv2.WINDOW_NORMAL)
cv2.namedWindow("blue",cv2.WINDOW_NORMAL)

cv2.imshow("red",r)
cv2.imshow("green",g)
cv2.imshow("blue",b)

img2=cv2.merge([b,g,r])
cv2.imshow("image2",img2)
