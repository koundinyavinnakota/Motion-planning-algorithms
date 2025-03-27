import sys
import os
from helper_node import *
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0,parent_dir)
from Environment.map import *
from a_star import astar
def plotPath(path_found,map):
    path = path_found[::-1]
    for i in path:
        cv2.circle(map, (i[0],i[1]),0,(0,255,0),-1)
        cv2.imshow("cunt node", map)
        cv2.waitKey(1)
        
def backtrack(node, start_node, path_found):
    # print(node.current_node)
    path_found.append(node.current_node)
    # print(path_found)
    
    if node.parent == start_node:
        # print(node.parent.current_node)
        path_found.append(node.parent.current_node)
        # print(path_found)
        return 
    else:
        backtrack(node.parent, start_node,path_found)

if __name__ == "__main__":
    start_time = time.time()
    new_map = get_map(1)
    
    # print(new_map.shape)
    start_node = Node(5,95)
    goal_node = Node(95,5)
    set_start_node(new_map,start_node.x,start_node.y)
    set_goal_node(new_map,goal_node.x,goal_node.y)
    # print(astar(start_node,goal_node,new_map)) 
    closed_list = astar(start_node,goal_node,new_map)
    goal_found = closed_list[-1]
    # print(goal_found.current_node)
    path_found = []
    backtrack(goal_found, start_node, path_found)
    end_time = time.time()
    print("Total Time : ", end_time - start_time)
    print(path_found)
    plotPath(path_found,new_map)
    
    
    # cv2.imshow("Map", new_map)
    cv2.waitKey(0)
    # cost_map = [1,1,1,1,1,1,1,1]
    # moves = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    
    

 

