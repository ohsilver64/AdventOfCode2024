import os
import re
from collections import defaultdict, Counter, deque

def readFile(path):
    with open(path,'r') as f:
        return f.read().strip()
os.chdir(os.path.dirname(os.path.abspath(__file__))) #ensure the script runs in its own directory)
input = readFile('input.txt')
count1 = 0
# E[x] is the set of pages that must come before x
# ER[x] is the set of pages that must come after x
E = defaultdict(set)
ER = defaultdict(set)

rules,queries = input.split('\n\n')
for rule in rules.split('\n'):
    left,right = rule.split('|')
    left,right = int(left), int(right)
    E[right].add(left)
    ER[left].add(right)

for list in queries.split('\n'):
    values = [int(v) for v in list.split(',')]
    assert len(values)%2 ==1 
    ok = True
    for i,x in enumerate(values):
        for j,y in enumerate(values):
            if i<j and y in E[x]:
                ok = False
    if ok:
        count1 += values[len(values)//2]
print(f'Problem one answer is: {count1}')


