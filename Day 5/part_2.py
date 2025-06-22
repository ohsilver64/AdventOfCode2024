import re
import os
from operator import itemgetter

def readFile(path):
    with open(path,'r') as f:
        return f.read()

def process(txt):
    lists = []
    rules = []
    for line in txt:
        if '|' in line:
            rule = [int(x) for x in line.split('|') if x.strip().isdigit()]
            rules.append(rule)
        if ',' in line:
            number_list = [int(x) for x in line.split(',') if x.strip().isdigit()]
            if len(number_list) == 0:
                continue
            else:
                lists.append(number_list) 
    return rules,lists


def extract_rules(lst, rules):
    rel_rules = []
    for left, right in rules:
        if left in lst and right in lst:
            rel_rules.append((left, right))
    return rel_rules

def assign_values(lst,rel_rules):
    rankings = {}
    for num in lst:
        rankings.update({num:0})
    for rule in rel_rules:
        left,right = rule
        rankings[left] += 1
        rankings[right] -= 1
    return rankings

def reorderdic(dic):
    # Get the original order of keys
    original_keys = list(dic.keys())
    # Get the keys sorted by value (descending)
    sorted_keys = [k for k, v in sorted(dic.items(), key=itemgetter(1), reverse=True)]
    if original_keys == sorted_keys:
        return 0
    # If not sorted, return the middle key
    median = (len(sorted_keys) - 1) // 2
    return sorted_keys[median]
                
def solveProblemOne(input):
    count = 0
    rules,lists = process(input)
    for line in lists:
        rel_rules = extract_rules(line,rules)
        ranking_dict = assign_values(line,rel_rules)
        middle_key = reorderdic(ranking_dict)
        count += middle_key
    return count


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__))) #ensure the script runs in its own directory)
    input = readFile('input.txt').splitlines()
    solution1 = solveProblemOne(input)
    print(f'The sum of middle values is {solution1}')
    

if __name__ == "__main__":
    main()
