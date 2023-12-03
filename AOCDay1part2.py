import re

from aocd import get_data
lines = get_data(day=1, year=2023).split("\n")

def NumberFinder(line, NumberDictionary):
    for i,value in enumerate(line):
        try:
            x = int(value)
            return x
        except:
            for key in NumberDictionary:
                if type(re.search(key,line[i:i+5])) != type(None):
                    x = NumberDictionary[key]
                    return x

NumberDictionary1 = {
    "one..":1,
    "two..":2,
    "three":3,
    "four.":4,
    "five.":5,
    "six..":6,
    "seven":7,
    "eight":8,
    "nine.":9
}

ReverseNumberDictionary1 = {
    "eno..":1,
    "owt..":2,
    "eerht":3,
    "ruof.":4,
    "evif.":5,
    "xis..":6,
    "neves":7,
    "thgie":8,
    "enin.":9
}

solution = 0
lineindex = 1

for line in lines:
    #find the location of the first integer written out
    x = NumberFinder(line, NumberDictionary1)
    y = NumberFinder(line[::-1], ReverseNumberDictionary1)
    solution += 10*x+y
    lineindex += 1
    print(line)
    print(lineindex, x, y, 10*x+y, solution)