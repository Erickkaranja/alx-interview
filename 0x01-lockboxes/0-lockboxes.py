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
