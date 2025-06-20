import pandas as pd
import numpy as np
import os

def readfile(path):
    with open(path, 'r') as f:
        return f.read()

def toDF(s):
    lines = [list(line) for line in s.splitlines() if line]
    return pd.DataFrame(lines)


def count_xmas(df):
    target = ['X','M','A','S']
    arr = df.to_numpy()
    rows, cols = arr.shape
    count = 0

    # eight directions: right, down, left, up, and the four diagonals
    dirs = [
        ( 0,  1),  # → 
        ( 1,  0),  # ↓
        ( 0, -1),  # ←
        (-1,  0),  # ↑
        ( 1,  1),  # ↘
        ( 1, -1),  # ↙
        (-1,  1),  # ↗
        (-1, -1),  # ↖
    ]

    for i in range(rows):
        for j in range(cols):
            # we only start a scan where there's an 'X'
            if arr[i, j] != 'X':
                continue

            for di, dj in dirs:
                # compute end-point of 4-letter word
                end_i = i + 3*di
                end_j = j + 3*dj
                # if out of bounds, skip
                if not (0 <= end_i < rows and 0 <= end_j < cols):
                    continue

                # collect the 4 letters along (di,dj)
                seq = [ arr[i + k*di, j + k*dj] for k in range(4) ]
                if seq == target:
                    count += 1

    return count

def countMas(df):
    arr = df.to_numpy()
    rows, cols = arr.shape
    count = 0

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if arr[i, j] != 'A':
                continue

            tl = arr[i-1, j-1]  # top-left
            tr = arr[i-1, j+1]  # top-right
            bl = arr[i+1, j-1]  # bottom-left
            br = arr[i+1, j+1]  # bottom-right

            # pattern M-A-S along ↘ and ↙
            diag1_fwd = (tl,   arr[i,j], br) == ('M','A','S')
            diag1_bwd = (tl,   arr[i,j], br) == ('S','A','M')

            # pattern M-A-S along ↙ and ↗
            diag2_fwd = (tr,   arr[i,j], bl) == ('M','A','S')
            diag2_bwd = (tr,   arr[i,j], bl) == ('S','A','M')

            if (diag1_fwd or diag1_bwd) and (diag2_fwd or diag2_bwd):
                count += 1

    return count
def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    raw = readfile('input.txt')
    df = toDF(raw)
    total = count_xmas(df)
    total2 = countMas(df)
    print(f'There are {total} instances of XMAS')
    print(f'There are {total2} instances of X-MAS')

if __name__ == '__main__':
    main()