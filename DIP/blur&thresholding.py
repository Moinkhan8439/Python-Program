import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("ch3\Fig0334(a)(hubble-original).tif",0)
ret,thresh1=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
ret,thresh4=cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV)
ret,thresh5=cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
plt.subplot(321),plt.imshow(img,'gray'),plt.title("normal image"),plt.axis("off")
plt.subplot(322),plt.imshow(thresh1,'gray'),plt.title("thresholded binary "),plt.axis("off")
plt.subplot(323),plt.imshow(thresh2,'gray'),plt.title("thresholded binary inversion"),plt.axis("off")
plt.subplot(324),plt.imshow(thresh3,'gray'),plt.title("thresholded  to Zero"),plt.axis("off")
plt.subplot(325),plt.imshow(thresh4,'gray'),plt.title("thresholded to Zero inv"),plt.axis("off")
plt.subplot(326),plt.imshow(thresh5,'gray'),plt.title("thresholded truncated"),plt.axis("off")
plt.show()
