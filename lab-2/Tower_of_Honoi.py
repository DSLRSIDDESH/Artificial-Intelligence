moves = []
def move(t1,t2,n):
    global moves
    moves.append(f"step-{len(moves)+1}: Move disc-{n} from {t1} to {t2}")

def recursive_ToH(start,inter,end,n):
    if n == 1:
        move(start,end,n)
        return
    recursive_ToH(start,end,inter,n-1)
    move(start,end,n)
    recursive_ToH(inter,start,end,n-1)

n = 3  #int(input("Enter the number of discs: "))
recursive_ToH("tower-1","tower-2","tower-3",n)
print("Using Recursion:")
for i in moves:
    print("   ",i)

t1,t2,t3,steps = [3,2,1],[],[],[]
for i in range(1,2**n):
    if i%3 == 1:
        if len(t3)==0 or (len(t1)!= 0 and t1[-1] < t3[-1]):
            steps.append(f"step-{i}: Move disc-{t1[-1]} from tower-1 to tower-3")
            t3.append(t1[-1])
            t1.pop(-1)
        elif len(t1)==0 or (len(t3)!=0 and t3[-1] < t1[-1]):
            steps.append(f"step-{i}: Move disc-{t3[-1]} from tower-3 to tower-1")
            t1.append(t3[-1])
            t3.pop(-1)
    elif i%3 == 2:
        if len(t2)==0 or (len(t1)!=0 and t1[-1] < t2[-1]):
            steps.append(f"step-{i}: Move disc-{t1[-1]} from tower-1 to tower-2")
            t2.append(t1[-1])
            t1.pop(-1)
        elif len(t1)==0 or (len(t2)!=0 and t2[-1] < t1[-1]):
            steps.append(f"step-{i}: Move disc-{t2[-1]} from tower-2 to tower-1")
            t1.append(t2[-1])
            t2.pop(-1)
    elif i%3 == 0:
        if len(t3)==0 or (len(t2)!=0 and t2[-1] < t3[-1]):
            steps.append(f"step-{i}: Move disc-{t2[-1]} from tower-2 to tower-3")
            t3.append(t2[-1])
            t2.pop(-1)
        elif len(t2)==0 or (len(t3)!=0 and t3[-1] < t2[-1]):
            steps.append(f"step-{i}: Move disc-{t3[-1]} from tower-3 to tower-2")
            t2.append(t3[-1])
            t3.pop(-1)
print("Without Recursion:")
for i in steps:
    print("   ",i)