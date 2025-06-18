import os
# a report is only safe if 
# a) the levels are either all increasing or decreasing
# b) the levels are seperated by a difference of between 1 and 3 

def readFile(path): #read a file and return its contents
    with open(path,'r') as f:
        return f.read()
def read_input(filename): #read a file and return each line as a list of integers
    with open(filename) as f:
        lines = f.readlines()
    return [[int(x) for x in line.strip().split()] for line in lines if line.strip()]

def isIncreasing(lst):  #these functions check if the list is strictly increasing or decreasing
    return all(x<y for x,y in zip(lst,lst[1:]))
def isDecreasing(lst):
    return all(x>y for x,y in zip(lst,lst[1:]))

def jumpSize(lst): #checks if the difference between each element is between 1 and 3
    if all(0<abs(x-y)<4 for x,y in zip(lst,lst[1:])):
        return True
    else:
        return False
    

def isSafe(lst): 
    if (isIncreasing(lst) or isDecreasing(lst)) and jumpSize(lst): #checks if the report is safe
        return True
    else:
        return False

def testBad(lst): #this function tests if removing an element from the list makes it safe. It loops over each element, removes it and checks if the remaining elements are safe
    if isSafe(lst):
        return True
    else:
        for i,num in enumerate(lst):
            lst.pop(i) #remove the element at index i
            if isSafe(lst):
                return lst
            else: 
                lst.insert(i,num) #put the element back in if it didn't work
        return False



def solveProblemOne(input):
    count = 0 
    for line in input:
        a = isIncreasing(line)
        b = isDecreasing(line)
        c = jumpSize(line)
        if (a or b) and c:
            count = count + 1
    return count


def solveProblemTwo(input):
    count = 0 
    for line in input:
        if testBad(line):
            count = count + 1
    return count

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__))) #ensure the script runs in its own directory
    input = read_input('input.txt')
    solution1 = solveProblemOne(input)
    solution2 = solveProblemTwo(input)
    print(f'There are {solution1} safe reports')
    print(f'There are {solution2} safe reports after removing a bad element')

if __name__ == "__main__":
    main()
