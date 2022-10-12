import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread("ch1\Fig0106(a)(bone-scan-GE).tif",0)
neg=255-img
cv2.imshow("Negative",neg)

img=cv2.imread("ch3\Fig0305(a)(DFT_no_log).tif",0)
c=255/np.log(1+np.max(img))
log_pic=c*(np.log(1+img))
log_pic=np.array(log_pic,dtype=np.uint8)
cv2.imshow("log",log_pic)

