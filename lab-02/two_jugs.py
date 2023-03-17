l = [0,0]
def fill(x,capacity):
    global l
    l[x] += capacity
def empty(x):
    global l
    l[x] = 0
def pour(x,y,capacity):
    global l
    if(l[x]+l[y]) <= capacity:
        l[y] = l[x]+l[y]
        l[x] = 0
    else:
        l[x] = l[x]+l[y] - capacity
        l[y] = capacity

steps = []
l1 = list(map(int,input("Enter the capacities of the jars: ").split()))
t = int(input("Enter the desired capacity to attain : "))
if(t<=0 or t>l1[1]):
    print("Not possible to attain that configuration")
else:
    i,j = 1,0
    while(t>0 and t<=l1[1] and j<=1000):
        if l[0]==t or l[1]==t:
            break
        if l[0] == 0:
            fill(0,l1[0])
            steps.append(f"step-{i}: Fill jug-1               : {l}")
            i += 1
            pour(0,1,l1[1])
            steps.append(f"step-{i}: Pour from jug-1 to jug-2 : {l}")
            i += 1
        else:
            pour(0,1,l1[1])
            steps.append(f"step-{i}: Pour from jug-1 to jug-2 : {l}")
            i += 1
        if l[1] == l1[1]:
            empty(1)
            steps.append(f"step-{i}: Empty the jug-2          : {l}")
            i += 1
        j += 1
    if j > 1000:
        print("Not possible to attain that configuration")
    else:
        print("Steps involved: ")
        for i in range(len(steps)):
            print(f"    {steps[i]}")