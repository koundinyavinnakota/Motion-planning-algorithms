import sys
import os
from helper_node import *
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0,parent_dir)
from Environment.map import *
from a_star import astar

def backtrack(node, start_node):
    # print(node.current_node)
    if node.parent == start_node:
        # print(node.parent.current_node)
        return
    else:
        backtrack(node.parent, start_node)

if __name__ == "__main__":
    start_time = time.time()
    new_map = get_map()
    
    # print(new_map.shape)
    start_node = Node(15,480)
    goal_node = Node(480,15)
    set_start_node(new_map,start_node.x,start_node.y)
    set_goal_node(new_map,goal_node.x,goal_node.y)
    # print(astar(start_node,goal_node,new_map)) 
    closed_list = astar(start_node,goal_node,new_map)
    goal_found = closed_list[-1]
    # print(goal_found.current_node)
    backtrack(goal_found, start_node)
    end_time = time.time()
    print("Total Time : ", end_time - start_time)
    
    
    # cv2.imshow("Map", new_map)
    # cv2.waitKey(0)
    # cost_map = [1,1,1,1,1,1,1,1]
    # moves = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    
    

 

