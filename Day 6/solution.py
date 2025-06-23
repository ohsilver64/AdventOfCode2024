import numpy as np
import os

DIRS = {                # row-offset, col-offset
    '^': (-1,  0),
    '>': ( 0,  1),
    'v': ( 1,  0),
    '<': ( 0, -1),
}
TURN_RIGHT = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

def read_file(path):
    with open(path) as f:
        return f.read().strip()

def make_array(text):
    return np.array([list(line) for line in text.splitlines()])

def step_once(pos, facing, grid):
    r, c = pos
    rows, cols = grid.shape
    dr, dc = DIRS[facing]
    nr, nc = r + dr, c + dc

    # 1) Forward step
    if not (0 <= nr < rows and 0 <= nc < cols):
        # would walk off the map → done
        return pos, facing, False
    if grid[nr, nc] != '#':
        # clear floor → move forward
        return (nr, nc), facing, True

    # 2) Blocked ⇒ turn right once
    new_face = TURN_RIGHT[facing]
    dr, dc = DIRS[new_face]
    nr, nc = r + dr, c + dc

    if not (0 <= nr < rows and 0 <= nc < cols):
        # after turning, the next step would leave the map
        return pos, new_face, False
    if grid[nr, nc] != '#':
        return (nr, nc), new_face, True

    # 3) Both forward squares are walls → stuck, so we quit
    return pos, new_face, False
def visited_count(grid):
    # find guard
    where = np.argwhere(np.isin(grid, list(DIRS.keys())))[0]
    pos = tuple(where)
    facing = grid[pos]
    visited = {pos}

    while True:
        pos, facing, moved = step_once(pos, facing, grid)
        if not moved:                            # next step would be off-map
            break
        visited.add(pos)

    return len(visited)

# --------------------------------------------------------------------
def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    grid = make_array(read_file('input.txt'))
    print(f'Distinct squares visited: {visited_count(grid)}')
if __name__ == "__main__":
    main()
