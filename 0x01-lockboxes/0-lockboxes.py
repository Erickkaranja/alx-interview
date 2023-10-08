#!/usr/bin/python3
'''lock boxes study question.'''
from collections import deque


def canUnlockAll(boxes):
    '''defining function canUnlockAll.'''
    n = len(boxes)
    visited = set()
    queue = deque([0])  # Start from the first box (box 0)

    while queue:
        current_box = queue.popleft()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited and key < n:
                queue.append(key)

    return len(visited) == n
