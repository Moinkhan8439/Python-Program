import cv2
import numpy as np
from matplotlib import pyplot as plt

img =cv2.imread("ch2\Fig0229(a)(tungsten_filament_shaded).tif",0)
shade =cv2.imread("ch2\Fig0229(b)(tungsten_sensor_shading).tif",0)
img=np.float64(img)
shade=np.float64(shade)

div=img/shade
plt.subplot(131),plt.imshow(img,'gray')
plt.subplot(132),plt.imshow(shade,'gray')
plt.subplot(133),plt.imshow(div,'gray')
plt.show()
