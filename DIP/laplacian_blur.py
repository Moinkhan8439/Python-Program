import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("ch3\Fig0338(a)(blurry_moon).tif",0)
k=np.array([[1,1,1,],[1,4,1],[1,1,1]])
l=cv2.filter2D(img,-1,k)
sharp=cv2.subtract(img,l)
plt.subplot(221),plt.imshow(img,'gray'),plt.title("normal image"),plt.axis("off")
plt.subplot(222),plt.imshow(l,'gray'),plt.title("laplacian image"),plt.axis("off")
plt.subplot(223),plt.imshow(sharp,'gray'),plt.title("sharp image"),plt.axis("off")
plt.show()
