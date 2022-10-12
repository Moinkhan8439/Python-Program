import cv2
from matplotlib import pyplot as plt
import numpy as np

img=cv2.imread("ch3\Fig0308(a)(fractured_spine).tif",0)
g1=3
g2=1.5
g3=0.5
img=img/255
new_img1=(img**g1)
new_img2=(img**g2)
new_img3=(img**g3)


new_img1=new_img1*255
new_img2=new_img2*255
new_img3=new_img3*255

new_img1=np.array(new_img1,dtype=np.uint8)
new_img2=np.array(new_img2,dtype=np.uint8)
new_img3=np.array(new_img3,dtype=np.uint8)

plt.subplot(221),plt.imshow(img,'gray'),plt.title("normal image"),plt.axis("off")
plt.subplot(222),plt.imshow(new_img1,'gray'),plt.title("gamma 3"),plt.axis("off")
plt.subplot(223),plt.imshow(new_img2,'gray'),plt.title("gamma 1.5"),plt.axis("off")
plt.subplot(224),plt.imshow(new_img3,'gray'),plt.title("gamma 0.5"),plt.axis("off")
plt.show()
