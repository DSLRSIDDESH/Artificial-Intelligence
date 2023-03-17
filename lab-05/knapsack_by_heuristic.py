capacity = 400
weights = (200, 10, 300, 1, 100)
profits = (5000, 1000, 4000, 5000, 2000)

def heuristic(path, capacity):      # heuristic used is the sum of the profits of the
    global weights, profits         # items not in the sack that can fit the remaining
    n = len(weights)                # capacity filled by comparing reletive profits
    all_tpls = []
    for i in range(n):
        if i not in path:
            all_tpls.append((profits[i]/weights[i],weights[i],profits[i]))
    all_tpls.sort(reverse=True)
    total_weight,total_profit = 0,0
    for tpl in all_tpls:
        if total_weight + tpl[1] <= capacity:
            total_weight += tpl[1]
            total_profit += tpl[2]
        else:
            break
    return total_profit

def a_star(weights, profits, capacity):
    n = len(weights)
    knapsack = [((), 0, 0)]
    
    for i in range(n):
        sack, weight, profit = knapsack.pop(0)
        not_include = (sack, weight, profit)
        if weights[i] <= capacity:
            include = (sack + (i,), weight+weights[i], profit+profits[i])
            heuristic_1 = heuristic(not_include[0]+(i,), capacity)
            heuristic_2 = heuristic(include[0], capacity - weights[i])
            f_1 = heuristic_1 + not_include[2]
            f_2 = heuristic_2 + include[2]

            if f_2 > f_1:
                knapsack.append(include)
                capacity -= weights[i]
            else:
                knapsack.append(not_include)
        else:
            knapsack.append(not_include)
    return (knapsack[0])

tupl = a_star(weights, profits, capacity)
print("The maximum profit : ", tupl[2])
print("The items in the knapsack : ", *tupl[0])
print("The total weight after knapsack is filled : ", tupl[1])