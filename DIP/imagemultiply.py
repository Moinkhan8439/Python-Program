import cv2
import numpy as np
from matplotlib import pyplot as plt

img =cv2.imread("ch2\Fig0230(a)(dental_xray).tif",0)
shade =cv2.imread("ch2\Fig0230(b)(dental_xray_mask).tif",0)
img=np.float64(img)
shade=np.float64(shade)

mul=img*shade
plt.subplot(131),plt.imshow(img,'gray')
plt.subplot(132),plt.imshow(shade,'gray')
plt.subplot(133),plt.imshow(mul,'gray')
plt.show()
