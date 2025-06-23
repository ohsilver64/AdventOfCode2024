import os


def readFile(path):
    with open(path,'r') as f:
        return f.read().splitlines()

def get_equations(input):
    equations = []
    for line in input:
        product,factors = line.split(': ')
        product = int(product)
        factors = [int(f) for f in factors.split(' ')]
        equations.append([product,factors])
    return equations


def line_is_good(target: int, nums: list[int]) -> bool:


    def dfs(idx: int, running: int) -> bool:
        if idx == len(nums):
            return running == target

        next_val = nums[idx]

        # 1) '+' branch
        if dfs(idx + 1, running + next_val):
            return True

        # 2) '*' branch
        if dfs(idx + 1, running * next_val):
            return True

        # 3) '||' branch  
        concat = int(f"{running}{next_val}")
        if dfs(idx + 1, concat):
            return True

        return False

    # start with first number already consumed
    return dfs(1, nums[0])

#def get_segments(target:int):
#    length = len(str(target))
#    segments = []
#    a=1
#    for num in range(length-1):
#        x = []
#        left = target // (10**(a))
#        right = target % (10**a)
#        a += 1
#        x.append(left)
#        x.append(right)
#        segments.append(x)
#    return segments



def main1():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    input = get_equations(readFile('input.txt'))
    summation = 0

    for line in input:
        target,nums = line
        if line_is_good(target,nums):
            summation += target
    print(f'The sum of good equation factors is: {summation}')

def getbad(input):
    bad = []
    for line in input:
        target,nums = line
        if not line_is_good(target,nums):
            bad.append(line)
    return bad

def main2():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    equations = get_equations(readFile("input.txt"))

    total = sum(
        target for target, nums in equations
        if line_is_good(target, nums)          # now includes '+', '*', '||'
    )

    print(f"Total calibration result: {total}")

if __name__ == "__main__":
    main1()
    main2()
