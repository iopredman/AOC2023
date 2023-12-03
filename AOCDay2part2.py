from aocd import get_data
lines = get_data(day=2, year=2023).split("\n")

SumPowers = 0

for line in lines:
    
    GameDictionary = {
    'red': 0,
    'green': 0,
    'blue': 0
    }
    
    line = list(line.split())
    length = len(line)
    for i, element in enumerate(line):
        element = element.strip(",;")
        if element in GameDictionary.keys():
            if int(line[i-1]) > GameDictionary[element]:
                GameDictionary[element] = int(line[i-1])
        if i+1 == length:
            Power = 1
            for value in GameDictionary.values():
                Power = Power*value
            SumPowers += Power

print(SumPowers)