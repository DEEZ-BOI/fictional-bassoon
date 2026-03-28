import heapq
from maze_solver.maze import get_neighbors


def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def astar(maze, start, goal):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in get_neighbors(node, maze):
            new_cost = len(path) + heuristic(neighbor, goal)
            heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))

    return None
