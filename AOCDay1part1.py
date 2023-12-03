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
