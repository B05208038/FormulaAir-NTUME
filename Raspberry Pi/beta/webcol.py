# Webcam image previewer
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
name = '0422im2age'

i = 1

while True:
	ret, frame = cap.read()
	cv2.imshow('fraxme', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		fname = name + str(i) + '.bmp'
		cv2.imwrite(fname,frame)
		i = i + 1
		print("capture image number: ",i)
		continue
	if i > 20:
		break

cap.release()
cv2.destroyAllWindows()
