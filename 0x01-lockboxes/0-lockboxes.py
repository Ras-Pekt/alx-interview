#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    """
    n = len(boxes)
    visited = [False] * n

    def breadth_first_search(box):
        """bfs algorithm"""
        visited[box] = True
        for next_box in boxes[box]:
            if not visited[next_box]:
                breadth_first_search(next_box)

    breadth_first_search(0)
    return all(visited)
