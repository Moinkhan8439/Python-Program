import cv2
import numpy as np
from matplotlib import pyplot as plt

img =cv2.imread("ch2\Fig0226(galaxy_pair_original).tif",0)
img=np.float64(img)
sum_=np.zeros((img.shape),np.float64)
mean=0
sd=30
for i in range(100):
    noise=np.random.normal(mean,sd,(img.shape))
    noise=img+noise
    sum_=sum_+noise
avg=sum_/i
plt.subplot(131),plt.imshow(img,'gray')
plt.subplot(132),plt.imshow(noise,'gray')
plt.subplot(133),plt.imshow(avg,'gray')
plt.show()
