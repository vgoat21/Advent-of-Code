import operator
with open('data.txt') as f:
    temp = f.read().splitlines()
depths = [int(i) for i in temp]
depths = list(map(operator.sub, depths[1:], depths[:-1]))
end = sum(x > 0 for x in depths)
print(end)