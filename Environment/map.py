import cv2
import numpy as np

scale = 3
c = 5 # Scale of the map
layout = np.zeros((100*c,100*c,3))

# Obstacle 1 
obs1 = np.array([[[25*c,100*c], [25*c,10*c],[30*c,10*c],[30*c,100*c]]])
cv2.fillPoly(layout,pts = [obs1],color = (255,255,255))

#obstacle 2
obs1 = np.array([[[75*c,0*c], [75*c,90*c],[80*c,90*c],[80*c,0*c]]])
cv2.fillPoly(layout,pts = [obs1],color = (255,255,255))

cv2.imshow(" layout ", layout)
cv2.waitKey(0)