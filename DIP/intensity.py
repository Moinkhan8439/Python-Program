import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("ch2/\Fig0221(a)(ctskull-256).tif",0)
x1=8
x2=4
x3=2
img=np.array(img).astype(np.uint8)
step1=np.ceil(255/(x1-1))
step2=np.ceil(255/(x2-1))
step3=np.ceil(255/(x3-1))

new_img1= np.round(img/step1)*step1
new_img2= np.round(img/step2)*step2
new_img3= np.round(img/step3)*step3

new_img1=new_img1.astype(np.uint8)
new_img2=new_img2.astype(np.uint8)
new_img3=new_img3.astype(np.uint8)

plt.subplot(221)
plt.imshow(img,"gray")
plt.title("normal image")
plt.axis("off")

plt.subplot(222)
plt.imshow(new_img1,"gray")
plt.title("8 intensity image")
plt.axis("off")

plt.subplot(223)
plt.imshow(new_img2,"gray")
plt.title("4 intensity  image")
plt.axis('off')

plt.subplot(224)
plt.imshow(new_img3,"gray")
plt.title("2 intensity image")
plt.axis('off')

plt.show()
