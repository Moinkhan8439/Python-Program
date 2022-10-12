import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('noise2.tif',0)
plt.subplot(141)
plt.imshow(img,cmap="gray")
plt.title("original")
plt.axis("off")

f = np.fft.fft2(img)
f2 = np.fft.fftshift(f)
f3 = 0.5*np.log(1+np.abs(f2))
plt.subplot(142)
plt.imshow(f3,cmap="gray")
plt.title("Fourier")
plt.axis("off")

m,n = img.shape
p,q = np.meshgrid(np.arange(-np.floor(m/2), np.floor(m/2)), np.arange(-np.floor(n/2), np.floor(n/2))) 
D= np.sqrt(p**2 + q**2)

d=180.1
W=15
#a=[D < (d-(W/2)),D>(d+(W/2))]
#C=a[0]<a[1]
#butterworth
C=1/(1+((D*W)/(D**2-d**2))**2)

hp=f2*C.T
i = np.fft.ifftshift(hp)
i2 = np.fft.ifft2(i)
i2 = np.abs(i2)
m = np.max(i2)
i2 = i2/m

plt.subplot(143)
plt.imshow(i2,cmap="gray")
plt.title("After band reject")
plt.axis("off")

C=1-C
hp1=f2*C.T
j = np.fft.ifftshift(hp)
j2 = np.fft.ifft2(j)
j2 = np.abs(j2)
m = np.max(j2)
j2 = j2/m


plt.subplot(144)
plt.imshow(j2,cmap="gray")
plt.title("After band pass")
plt.axis("off")
plt.show()