def get_neighbors(pos, maze):
    x, y = pos
    moves = [(0,1),(1,0),(0,-1),(-1,0)]
    neighbors = []

    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#':
            neighbors.append((nx, ny))

    return neighbors
