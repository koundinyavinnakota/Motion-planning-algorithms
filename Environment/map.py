import cv2
import numpy as np


def get_map(c=5):
    # scale = 3
    layout = np.zeros((100*c,100*c,3))
    # Obstacle 1 
    obs1 = np.array([[[25*c,100*c], [25*c,10*c],[30*c,10*c],[30*c,100*c]]])
    cv2.fillPoly(layout,pts = [obs1],color = (255,255,255))

    #obstacle 2
    obs1 = np.array([[[75*c,0*c], [75*c,90*c],[80*c,90*c],[80*c,0*c]]])
    cv2.fillPoly(layout,pts = [obs1],color = (255,255,255))
    return layout
    # cv2.imshow(" layout ", layout)
    # cv2.waitKey(0)
    
def set_start_node(map,x,y):
    cv2.circle(map, (x,y),5,(0,255,0),-1)

def set_goal_node(map,x,y):
    cv2.circle(map, (x,y),5,(0,0,255),-1)    
    
def isObstacle(map,x,y): 
    print(map[x,y,:])
    if np.array_equal(map[499-y,x,:], [255,255,255]):
        print("Obstacle space")
        return True
    return False