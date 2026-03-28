from collections import deque
from maze_solver.maze import get_neighbors


def bfs(maze, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in get_neighbors(node, maze):
            queue.append((neighbor, path + [neighbor]))

    return None
