import cv2,time
video = cv2.VideoCapture(0)
check,frame=video.read()
time.sleep(1)
cv2.imshow("Capture",frame)
cv2.waitKey(3000)
video.release()
cv2.destroyAllWindows()
