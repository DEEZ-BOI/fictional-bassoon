def print_maze_with_path(maze, path):
    maze_copy = [row[:] for row in maze]

    for x, y in path:
        if maze_copy[x][y] not in ['S', 'G']:
            maze_copy[x][y] = '*'

    for row in maze_copy:
        print(" ".join(row))
