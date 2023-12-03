from aocd import get_data
lines = get_data(day=2, year=2023).split("\n")

GameDictionary = {
    'red': 12,
    'green': 13,
    'blue': 14
}

SumID = 0

for line in lines:
    line = list(line.split())
    length = len(line)
    for i, element in enumerate(line):
        element = element.strip(",;")
        if element in GameDictionary.keys():
            if int(line[i-1]) > GameDictionary[element]:
                break
        if i+1 == length:
            SumID += int(line[1].strip(':'))

print(SumID)
