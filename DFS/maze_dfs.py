# -*- coding: utf-8 -*-
"""MAZE_DFS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-WBHtAhIBCX41oINLSd7wTeCrgM2P7q_
"""

class Solution:
    def hasPath(self, maze, start, destination) :
        m, n, visit = len(maze), len(maze[0]), set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        stack = [start]
        while stack:
            curx, cury = stack.pop()
            if [curx, cury] == destination:
                    return True
            for dirx, diry in directions:
                tx, ty = curx, cury
                while 0 <= tx + dirx < m and 0 <= ty + diry < n and not maze[tx + dirx][ty + diry]:
                    tx, ty = tx + dirx, ty + diry
                if (tx, ty) not in visit:
                    visit.add((tx, ty))
                    stack.append((tx, ty))
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