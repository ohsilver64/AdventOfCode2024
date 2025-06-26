import numpy as np
import os
from itertools import combinations
from math import gcd

# ──────────────────────────────────────────
def readFile(path):
    with open(path, "r") as f:
        return f.read().strip()

def make_array(text):
    return np.array([list(line) for line in text.splitlines()])

def check_matches(arr, row, col):
    """Other antennas with same char, but only those 'after' (row,col)."""
    char  = arr[row, col]
    coords = [tuple(rc) for rc in np.argwhere(arr == char)]
    return [(r, c) for r, c in coords if (r, c) > (row, col)]

def antinode_coords_part1(arr, a, b):
    """Return the two 1:2-ratio antinodes for unordered pair (a,b)."""
    r1, c1 = a
    r2, c2 = b
    dr, dc = r2 - r1, c2 - c1     

    out = []
    left = (r1 - dr, c1 - dc)
    if 0 <= left[0] < arr.shape[0] and 0 <= left[1] < arr.shape[1]:
        out.append(left)
    right = (r2 + dr, c2 + dc)
    if 0 <= right[0] < arr.shape[0] and 0 <= right[1] < arr.shape[1]:
        out.append(right)
    return out

def solve_part1(raw_text):
    arr = make_array(raw_text)
    antinodes = set()
    for r in range(arr.shape[0]):
        for c in range(arr.shape[1]):
            if arr[r, c] == ".":              # skip empty cells
                continue
            for other in check_matches(arr, r, c):
                antinodes.update(antinodes_part1 := antinode_coords_part1(arr, (r, c), other))
    return len(antinodes)

def antinode_coords_line(arr, a, b):
    r1, c1 = a
    r2, c2 = b
    dr, dc = r2 - r1, c2 - c1
    g = gcd(abs(dr), abs(dc))          # reduce step to minimal integer vector
    step_r, step_c = dr // g, dc // g

    # Walk in the negative direction from a
    r, c = r1, c1
    while 0 <= r < arr.shape[0] and 0 <= c < arr.shape[1]:
        yield (r, c)
        r -= step_r
        c -= step_c

    r, c = r1 + step_r, c1 + step_c
    while 0 <= r < arr.shape[0] and 0 <= c < arr.shape[1]:
        yield (r, c)
        r += step_r
        c += step_c

def solve_part2(raw_text):
    arr = make_array(raw_text)
    antinodes = set()

    # Group antenna coordinates by frequency character
    freq_dict = {}
    for (r, c), ch in np.ndenumerate(arr):
        if ch != ".":
            freq_dict.setdefault(ch, []).append((r, c))

    for coords in freq_dict.values():
        if len(coords) < 2:
            continue                       # single antenna → no lines
        for a, b in combinations(coords, 2):
            antinodes.update(antinodes_line := antinode_coords_line(arr, a, b))

    return len(antinodes)

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    raw = readFile("input.txt")

    print("Part 1 — unique antinode count:", solve_part1(raw))
    print("Part 2 — unique antinode count:", solve_part2(raw))

if __name__ == "__main__":
    main()