#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    number_of_boxes = len(boxes)
    open_boxes = [False for i in range(number_of_boxes)]
    open_boxes[0] = True

    keys = boxes[0]

    while True:
        """iterating through the boxes"""
        new_keys = []

        for key in keys:
            """iterating through the keys in each box"""
            if key < number_of_boxes and open_boxes[key] is False:
                open_boxes[key] = True
                new_keys.extend(boxes[key])

        if not new_keys:
            break

        keys.extend(new_keys)

    return all(open_boxes)
