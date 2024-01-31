#!/usr/bin/python3
'''lock boxes study question.'''


def canUnlockAll(boxes):
    '''defining function canUnlockAll.'''
    check_list = [i for i in range(1, len(boxes))]
    for i in range(0, len(boxes)):
        for key in boxes[i]:
            if key != i:
                if key in check_list:
                    check_list.remove(key)
    if len(check_list) == 0:
        return True
    return False

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
