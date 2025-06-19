import re
import os

test = """what()-%*;[mul(826,659)what()&mul(622,241)}^from();why()mul(499,923))mul(589,186)~how()why()]/~who()}mul(57,224)* ##[[*>mul(206,45)select(){~from(63,961)+!/'@mul(365,743)^ """

def readFile(filepath): # Read the contents of a file
    with open(filepath,'r') as f:
        return f.read()

def findMul(line): # Find all 'mul' expressions in a line
    index = re.findall(r'mul\(\d+,\d+\)', line)
    index = [i.replace('mul(','').replace(')','') for i in index]
    return index

def countMuls(lst): # Count the total value of all 'mul' expressions
    count = 0
    for i in lst:
        try:

            parts = i.split(',')

            val = int(parts[0]) * int(parts[1])
            count += val
        except:
            pass
    #print(f'linecount:{count}')
    return count

def solveProblemOne(input):
    count = 0
    
    muls = findMul(input)
    linecount = countMuls(muls)
    count += linecount
    return count

def solveProblemTwo(input):
    count = 0
    pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"
    instructions = re.findall(pattern, "".join(input))
    enabled = True

    for instr in instructions:
        match instr[0]:
            case 'do()':
                enabled = True
            case 'don\'t()':
                enabled = False
            case _ if enabled:
                count += countMuls(findMul(instr[0]))

    return count

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__))) #ensure the script runs in its own directory)
    lines = readFile('input.txt')
    solution1 = solveProblemOne(lines)
    solution2 = solveProblemTwo(lines)
    print(f'Problem one output: {solution1}')
    print(f'Problem two output: {solution2}')

if __name__ == '__main__':
    main()