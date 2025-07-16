import pandas as pd
import os


def readfile(path):
    with open(path,'r') as f:
        return f.read()

def convertList(inp):
    for i,num in enumerate(inp):
        slice = []
        if i %2 == 0 and num != 0:
            for j in range(num):
                slice.append(int(i/2))
        if i %2 == 1 and num != 0:
            for j in range(num):
                slice.append('.')
        inp[i] = slice
    return inp

def flattenList(inp):
    return [item for sublist in inp for item in sublist]


def correctList(inp):
    left,right = 0, len(inp) - 1
    while left < right:
        if inp[left] != '.': #if left isnt a dot, move on
            left += 1
        elif inp[right] == '.':
            right -= 1
        else:
            inp[left], inp[right] = inp[right], inp[left]
            left += 1
            right -= 1
    return inp
                    
def sumFiles(inp):
    count = 0
    for i, num in enumerate(inp):
        if num != '.':
            count += num * i
    return count
#2333133121414131402 becomes 00...111...2...333.44.5555.6666.777.888899
#becomes 0099811188827773336446555566..............
test = [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2]

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    inp = list(map(int, list(readfile('input.txt'))))
    result = flattenList(convertList(inp))
    corrected = correctList(result)
    sumfiles = sumFiles(corrected)
    print(sumfiles)
    

if __name__ == "__main__":
    main()