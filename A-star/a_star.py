from helper_node import *
from queue import PriorityQueue
import sys
import os,cv2
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0,parent_dir)
from Environment.map import isObstacle

def calculateTotalCost(node,goal_node,c2c):
    
    node.g = c2c + node.parent.g
    node.h = np.sqrt((node.x - goal_node.x)**2 + (node.y - goal_node.y)**2)
    # node.h = 0
    node.f = node.g + node.h
    return node.f
def checkInOpenList(openlist, node):
    for i in openlist.queue:
        if i[1].current_node == node.current_node:
            if i[1].f > node.f:
                # i[1] = node
                # i[0] = node.f
                i = (node.f,node)
            return True
    return False
def checkInClosed(closedlist,node):
    for i in closedlist:
        if i.current_node == node.current_node:
            return True
    return False

    
def astar(start_node,goal_node,map):
    cost_map = [1,1,1,1,1,1,1,1]
    moves = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    open_list = PriorityQueue()
    
    closed_list = []
    open_list.put((0,start_node))
    goal_reached = False
    
    while(not open_list.empty() and not goal_reached):
        # print("Inside While")
        cur_node = open_list.get()
        
        for c2c,i in enumerate(moves):
            
            if (cur_node[1].x + i[0] >= 0 and cur_node[1].x + i[0] < map.shape[1]) and \
            (cur_node[1].y + i[1] >= 0 and cur_node[1].y + i[1] < map.shape[0]) and \
                not isObstacle(map,cur_node[1].x + i[0],cur_node[1].y + i[1]):
                temp_node = Node(cur_node[1].x + i[0], cur_node[1].y + i[1])
                temp_node.updateParent(cur_node[1])
                if temp_node.current_node == goal_node.current_node:
                    # closed_list.append(goal_node)
                    print("Horray Goal Reached!")
                    goal_reached = True
                    goal_node = temp_node
                    break
                if checkInClosed(closed_list,temp_node):
                    continue
                   
                if checkInOpenList(open_list,temp_node): 
                    continue
                else:
                    # print(calculateTotalCost(temp_node,goal_node,cost_map[c2c]))
                    open_list.put((calculateTotalCost(temp_node,goal_node,cost_map[c2c]),temp_node))
                    cv2.circle(map, (temp_node.x, temp_node.y),0,(255,0,0),-1)
                    cv2.imshow("cunt node", map)
                    cv2.waitKey(1)                    
        closed_list.append(cur_node[1])
        if goal_reached:
            closed_list.append(goal_node)
        
    # cv2.waitKey(0)
    return closed_list
                
                
                
        
   

