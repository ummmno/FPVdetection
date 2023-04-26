import cv2
import numpy as np

i = 0

def findCross(img):
	img = img[100:img.shape[0]-100, 0:img.shape[1]]

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	blur = cv2.GaussianBlur(gray, (5,5), 0)

	thresh = cv2.threshold(blur, 110, 255, cv2.THRESH_BINARY)[1]
	lol = img
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for cnt in contours:
			area = cv2.contourArea(cnt)
			if area > 50 and cnt.size > 30:
					approx = cv2.approxPolyDP(cnt, 0.03 * cv2.arcLength(cnt, True), True)
					if len(approx) > 9 and len(approx) < 1000:
							cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)
							global i
							cv2.imwrite("./images/" + str(i) + "_" + str(cnt.size) + ".jpg", cv2.drawContours(lol, [cnt], 0, (0, 255, 0), 3))
							i += 1
							print("Cross detected")

	print("len" + str(len(contours)))
        
	return img

def videoPlay():
	cap = cv2.VideoCapture('trimmed.mp4')
		
	if (cap.isOpened()== False):
			print("Error opening video file")
		
	while(cap.isOpened()):
				
			ret, frame = cap.read()
			if ret == True:
					cv2.imshow('Frame', findCross(frame))
						
					if cv2.waitKey(25) & 0xFF == ord('q'):
							break
			else:
					break
			
	cap.release()
	cv2.destroyAllWindows()

#cv2.imshow("pic", findCross(cv2.imread("dronepic.jpg")))
#cv2.waitKey(0)

videoPlay()