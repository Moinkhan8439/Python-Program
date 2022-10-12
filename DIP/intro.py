import cv2

img=cv2.imread("background.jpg")
cv2.namedWindow("Image1",cv2.WINDOW_NORMAL)
cv2.imshow("Image1",img)

k=cv2.waitKey(0)
if k== ord('s'):
    cv2.imwrite("newimg.png",img)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()
