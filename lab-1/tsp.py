infi = float('inf')

graph = [
    [infi,12,10,19,8],
    [12,infi,3,7,6],
    [10,3,infi,2,20],
    [19,7,2,infi,4],
    [8,6,20,4,infi]
    ]

li = []
def all_paths(n,m,l):
    global li
    l1 = [i for i in l]
    l1.append(m)
    if len(l1) == n:
        li.append(l1)
        return
    for i in range(n):
        if i not in l1:
            all_paths(n,i,l1)
            
all_paths(len(graph),0,[])
cost_list = []

for i in li:
    cost = 0
    for j in range(len(i)-1):
        cost += graph[i[j]][i[j+1]]
    cost += graph[i[0]][i[-1]]
    cost_list.append(cost)
    
print("minimum Cost:",min(cost_list))
print("Travelling Sales Man Path :",li[cost_list.index(min(cost_list))])