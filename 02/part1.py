import operator
with open('data.txt') as f:
    temp = f.read().split()
instructions = [i for i in temp if not i.isdigit()]
values = [int(i) for i in temp if i.isdigit()]
x = 0
z = 0
for i in range(len(values)):
    if(instructions[i]=="forward"):
        x = x + values[i]
    elif(instructions[i]=="up"):
        z = z - values[i]
    elif(instructions[i]=="down"):
        z = z + values[i]
print(x*z)