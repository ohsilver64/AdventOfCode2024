import os
from collections import Counter

def readFile(path): # Reads the input file and returns its content as a string
    with open(path, 'r') as f:
        return f.read()


def findLists(input): # Parses the input string and returns two lists of integers
    data = [
        list(map(int, line.split()))
        for line in input.strip().split('\n')
    ]
    list1 =[]
    list2 = []
    for duo in data:
        list1.append(duo[0])
        list2.append(duo[1])
    return list1, list2

def sortLists(*lists): # Sorts each list in the input lists, required for Q1
    for list in lists:
        list.sort()
    return lists

def countDiff(*lists): # Counts the absolute difference between corresponding elements of two lists
    list1, list2 = lists
    count = 0
    for i in range(len(list1)):
        diff = abs(list1[i] - list2[i])
        count = count + diff
    return count

def findSimilarityScore(*lists): # Calculates the similarity score between two lists based on the frequency of elements
    list1, list2 = lists
    freq2 = Counter(list2)
    return sum(x * freq2.get(x, 0) for x in list1)



def solveProblemOne(input_str):
    return countDiff(*sortLists(*findLists(input_str)))

def solveProblemTwo(input_str):
    return findSimilarityScore(*findLists(input_str))

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__))) #ensure the script runs in its own directory
    input = readFile('input.txt')
    result1 = solveProblemOne(input)
    result2 = solveProblemTwo(input)
    print(f"Result of Problem One: {result1}")
    print(f"Result of Problem Two: {result2}")

if __name__ == "__main__":
    main()