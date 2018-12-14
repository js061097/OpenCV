import cv2
img = cv2.imread("C:\\Users\\Jason\\Desktop\\th.jpg",1)
resized=cv2.resize(img,(int(len(img[0])/2),int(len(img)/2)))
cv2.imshow("Legend",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
