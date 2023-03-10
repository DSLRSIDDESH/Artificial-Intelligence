#Travelling Salesman Problem using Simulated Annealing
import random
import math
import matplotlib.pyplot as plt

def ecldDist(x,y):  # function to fing Euclidean Distance
    x1 = math.pow(x[0]-y[0], 2)
    y1 = math.pow(x[1]-y[1], 2)
    dist = math.pow(x1 + y1, 0.5)
    return round(dist, 4)

def Cities(cities): # function to generate fifteen random city points in the given grid
    while len(cities) < 15: 
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        if (x,y) not in cities:
            cities.append((x,y))
    return cities

def totalDist(cities):  # funtion to find the cost or total distance for given solution
    dist = 0
    for i in range(len(cities)-1):
        dist += ecldDist(cities[i], cities[i+1])
    dist += ecldDist(cities[0], cities[-1])
    return round(dist,4)

def simulatedAnnealing(cities): # function in which we are performing Simmulated Annealing
    t0, temp = 0.1, 10**10
    alpha = 0.97
    prob = random.uniform(0.5,1)
    energy,itr = 1,0
    itr_list,dists = [],[]
    while temp > t0 :
        dup = cities[:]
        i,j = random.sample(range(1,10),k=2)
        dup[i], dup[j] = dup[j], dup[i]
        E0 = totalDist(cities)
        E1 = totalDist(dup)
        c = E1 - E0
        energy = math.exp(-c/temp)
        if c <= 0 or energy > prob:
            cities = dup[:]
        itr_list.append(itr)
        dists.append(totalDist(cities))
        itr += 1
        temp *= alpha
    plt.plot(itr_list,dists)
    plt.title('Iterations Vs Cost')
    plt.xlabel('Iterations')
    plt.ylabel('Cost or Distance')
    plt.show()         # plotting Iterations Vs Cost
    return cities
            
if __name__ == '__main__': 
    cities = Cities([])
    new_cities = simulatedAnnealing(cities)
    # Initial solution is order of cities that are originally generated randomly
    print('\nInitial Solution of path : ', *cities)
    print('Final Solution of path : ', *new_cities)
    print("\nInitial Cost :", totalDist(cities))
    print("FInal Cost   :", totalDist(new_cities), "\n")