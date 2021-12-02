import operator
with open('data.txt') as f:
    temp = f.read().splitlines()
depths = [int(i) for i in temp]
depths = [sum(depths[i:i+3]) for i in range(len(depths))]
depths = list(map(operator.sub, depths[1:], depths[:-1]))
end = sum(x > 0 for x in depths)
print(end)