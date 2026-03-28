from maze_solver.maze import get_neighbors


def dfs(maze, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in get_neighbors(node, maze):
            stack.append((neighbor, path + [neighbor]))

    return None
