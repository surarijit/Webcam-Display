"""to capture video from the webcam """

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
i=0
"""a =[1,2,3]
a = np.array(a)
print(type(a)) """

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read() 

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # draw a line
    cv2.line(gray,(0,0),(511,511),(255,0,0),5)
    rows,cols = gray.shape
    i=i+1
    if i==111 :
	i = 0
  
    if i%2==0:
     M = cv2.getRotationMatrix2D((cols/2,rows/2),0.05*i,1)
    else:
     M = cv2.getRotationMatrix2D((cols/2,rows/2),-0.05*i,1)
     
    dst = cv2.warpAffine(gray,M,(cols,rows))

    # Display the resulting frame
    cv2.imshow('frame',dst)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
