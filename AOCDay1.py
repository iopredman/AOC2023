# set AOC_SESSION=53616c7465645f5fa0936830c57b4acaf3a7ee8d899e6108bf28e26cb66329eb2347017d9b2b824175323f06addfba173b99283d716ed00ddea5e7453f74b401

from aocd import get_data
lines = get_data(day=1, year=2023).split("\n")

solutionlist = []

for line in lines:
    for i in line:
        try:
            x = int(i)
            break
        except:
            pass
    for i in line[::-1]:
        try:
            y = int(i)
            break
        except:
            pass
    solutionlist.append(x*10+y)

solution = sum(solutionlist)
print(solution)      