# -*- coding: utf-8 -*-
"""MAZE_BFS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cxt_25xxWM33Hu3GdMGhQaQZxNAqdkTI
"""

import collections
class Solution:
    def hasPath(self, maze, start, destination) :
        m = len(maze)
        n = len(maze[0])

        Q = collections.deque()     
        Q.append(start)

        Dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while(Q):

            x0, y0 = Q.popleft()

            for dir in Dir:
                x = x0 + dir[0]
                y = y0 + dir[1]

                while (x >= 0 and x < m and y >= 0 and y < n and maze[x][y] != 1):
                    x += dir[0]
                    y += dir[1]

                x = x - dir[0]
                y = y - dir[1]

                if x == destination[0] and y == destination[1]:
                    return True

                if maze[x][y] == 0:
                    Q.append((x, y))
                    maze[x][y] = 2

        return False

        
maze = [[0,0,1,0,0],
[0,0,0,0,0],
[0,0,0,1,0],
[1,1,0,1,1],
[0,0,0,0,0]]

start = [0,4]
destination = [4,4]
print('Test 1: ',Solution.hasPath((),maze,start,destination))


maze = [[0,0,1,0,0],
[0,0,0,0,0],
[0,0,0,1,0],
[1,1,0,1,1],
[0,0,0,0,0]]

start = [0,4]
destination = [3,2]
print('Test 2: ',Solution.hasPath((),maze,start,destination))

maze = [[0,0,0,0,0],
[1,1,0,0,1],
[0,0,0,0,0],
[0,1,0,0,1],
[0,1,0,0,0]]

start = [4,3]
destination = [0,1]
print('Test 3: ',Solution.hasPath((),maze,start,destination))