import pandas as pd
import numpy as np
import os

def readfile(path):
    with open(path,'r') as f:
        return f.read()

def toDF(string):
    data = string
    lines = [list(line) for line in data.split('\n') if line.strip()]
    df = pd.DataFrame(lines)
    return df

test = """
MAMAMASXXXSAMXSSSSSXMXMAMMSXMASAMXMXSSXMXXXXMSMSSMXXSAXMMSSSMSXMMXSMMMMSSMMMAMMMMSMMSXMAXMASMMSXASXSAMXXAAMXMXMAMXMAAXMASXSMXSSSSSSSSXMXSAMX
MSMMMMSXAAAMSMMAAMMMMAMASXMASAMMSXAXXMAMSMMMMXAMAMXAMMXSAAAAASASMASXAAMXAAXSAMAMMAAXXAMXMMSMMXMAMSAMXMMMSMMAXXXMXSMSMSMASMSMAMAAAAAAXXSASAAX
XAAXMAMMSMMMSAMMMMXAMAMXAAXAMXSAMAMXMSXMAASASMSMAMMXXAAMXMSMMSAMMAMXMXSXSMMMASMXSSMMMAMAAMAAASXSAMXMAXSAAAMSSSMMAAAASAMXXAMMAMAMMMMMMMMASMMS
SSXMMAXAAXMASMMXSXSMSSSSSXMSSMMXSAMXXAAXSMSASAMAMXXMMMXXAMXXXMXMMSXMSAXMAMXSXMXAAMXSASMMSXXMMAAXMXXSAXMMMSAAAXAASMMMSXSSMSMSASXSMXAXASMMMMAX
XXASMSSSMMMMSAMAMAXMAAMAMXMAAXAAMMMMMSSMAAMMMMMSSSSXSAASMSAXSAMXXXAAMAMSAMXSXAMMMMASAMAXMMMSAMXMSAMASXAAAMMMMMAMMAXXXAAAAMASASXAMSMSMSXXAMXM
MSXMAAAAXMSAMAMXSAMAMSMSMMXSMMMXSAXAAAXXMMMXMXMAAXAAMMXSAAMSMAMSAMMMMAMSASAMMSMSAMXSASXMSAAAAXSXMASAAXSMXMMASMMSSSMXMMMSSMAMAMMMMSAAXMAMSXSA
ASMMMMAMAXMASMMMMASMXAXAMXAAAXMASXSMSXSSXSAMXAMMSMMMMSMMXMMMXAMXXSAMSSMXAMMSMXASMSASAMXXMMSSSMMXSXMASMXMSMSASAAXMASXXXAAXMAXAASXMMSMSMXSAAAS
"""

#df = toDF(test)

def findLetter(index,col, df):
    try:
        X = df.iloc[index,col]
        return X
    except:
        return None

def isXmas(lst):
    if lst == ['X', 'M', 'A', 'S']:
        return True
    else:
        return False


def check_right(i, j, df):
    if j + 3 >= df.shape[1]:
        return False
    return df.iloc[i, j:j+4].tolist() == ['X','M','A','S']

def check_left(i, j, df):
    if j - 3 < 0:
        return False
    return df.iloc[i, j-3:j+1].tolist() == ['X','M','A','S']

def check_down(i, j, df):
    if i + 3 >= df.shape[0]:
        return False
    return df.iloc[i:i+4, j].tolist() == ['X','M','A','S']

def check_up(i, j, df):
    if i - 3 < 0:
        return False
    return df.iloc[i-3:i+1, j].tolist() == ['X','M','A','S']
    

# Diagonal sweeps using numpy.diag
def countDiag1(df):
    arr = df.to_numpy()
    rows, cols = arr.shape
    count = 0
    for k in range(-rows+1, cols):
        diag = np.diag(arr, k=k).tolist()
        for idx in range(len(diag) - 3):
            window = diag[idx:idx+4]
            if window == ['X','M','A','S'] or window == ['S','A','M','X']:
                count += 1
    return count

def countDiag2(df):
    arr = np.fliplr(df.to_numpy())
    rows, cols = arr.shape
    count = 0
    for k in range(-rows+1, cols):
        diag = np.diag(arr, k=k).tolist()
        for idx in range(len(diag) - 3):
            window = diag[idx:idx+4]
            if window == ['X','M','A','S'] or window == ['S','A','M','X']:
                count += 1
    return count

def solveProblemOne(df):
    total = 0
    rows, cols = df.shape
    for i in range(rows):
        for j in range(cols):
            if df.iat[i, j] != 'X':
                continue
            # check the four straight directions
            if check_right(i, j, df): total += 1
            if check_left(i, j, df):  total += 1
            if check_down(i, j, df):  total += 1
            if check_up(i, j, df):    total += 1
    # add diagonal counts
    total += countDiag1(df)
    total += countDiag2(df)
    return total

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__))) #ensure the script runs in its own directory)
    input = toDF(readfile('input.txt'))
    print(input)
    solution1 = solveProblemOne(input)
    print(f'There are {solution1} instances of XMAS')

if __name__ == "__main__":
    main()
    