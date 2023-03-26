import numpy as np

def print_tiles(tiles):
    # tiles = tiles.tolist()
    for i in range(len(tiles)):
        for j in range(len(tiles)):
            if tiles[i][j] == 0:
                tiles[i][j] = ' '
    print('  ',tiles[0][0],'|',tiles[0][1],'|',tiles[0][2])
    print('   --+---+--')
    print('  ',tiles[1][0],'|',tiles[1][1],'|',tiles[1][2])
    print('   --+---+--')
    print('  ',tiles[2][0],'|',tiles[2][1],'|',tiles[2][2])
    print()
    
def misplaced_tiles(puz, fin):
    return np.sum((puz != fin) & (puz != 0))

def dist_to_place(puz, fin):
    n = len(fin)
    h_n = 0     # Sum of the tile distances from goal
    for i in range(n):
        for j in range(n):
            if puz[i, j] != 0:
                row, col = np.where(fin == puz[i, j])
                h_n += abs(i - row[0]) + abs(j - col[0])
    return h_n
def a_star(puzzle, final, heuristic_type,h_type):
    
    org_puzzle = np.copy(puzzle)
    openList = []
    f1_n = misplaced_tiles(puzzle, final)
    closedList = [(puzzle.tolist(),f1_n,' ')]
    depth = 1
    n = len(final)
    while not (puzzle == final).all():
        neighbours = []
        x1,y1 = np.where(puzzle == 0)
        x,y = (x1[0],y1[0])
        if x > 0:
            neighbours.append((x-1, y))
        if y < n-1:
            neighbours.append((x, y+1))
        if x < n-1:
            neighbours.append((x+1, y))
        if y > 0:
            neighbours.append((x, y-1))

        neigh_child = []
        for i in neighbours:
            new_puz = np.copy(puzzle).tolist()
            new_puz[x][y],new_puz[i[0]][i[1]] = new_puz[i[0]][i[1]],new_puz[x][y]
            g_n = depth
            h_n = heuristic_type(np.array(new_puz), final)
            f_n = g_n + h_n
            child = [new_puz,f_n,puzzle.tolist()]
            neigh_child.append(child)

        for i in neigh_child:
            if i not in closedList:
                openList.append(i)
        idx,mn = 0,openList[0][1]
        
        for i in range(len(openList)):
            if openList[i][1] < mn:
                idx,mn = i,openList[i][1]

        puzzle = np.array(openList[idx][0])
        closedList.append(openList[idx])
        openList.pop(idx)

        depth += 1
    
    path = []
    path.append(closedList[-1][0])
    item = closedList[-1][0]
    while item != org_puzzle.tolist():
        index = 0
        for i, sublist in enumerate(closedList):
            if item == sublist[0]:
                index = i
                break
        path.append(closedList[index][2])
        item = closedList[index][2]
    print(f'\n--- Path or Moves using Heuristic-{h_type} ---\n')
    print('Initial State :\n')
    print_tiles(org_puzzle.tolist())
    move = 1
    for i in range(len(path)-2,-1,-1):
        print(f'Move-{move} :\n')
        print_tiles(path[i])
        move += 1
    print(f'Number of Moves : {len(path)-1}')
    print(f'Using Heuristic-{h_type} completed!')

if __name__ == '__main__':
    
    print("\nBelow I've provided path or moves for two heuristics separately!")
    puzzle = np.array([
        [2, 8, 3],
        [1, 6, 4],
        [7, 0, 5]
        ])
    
    final = np.array([
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
        ])
    
    a_star(puzzle,final,misplaced_tiles,'1') # for heuristic-1 (i.e. no. of misplaced tiles)
    a_star(puzzle,final,dist_to_place,'2')  # for heuristic-2 (i.e. sum of distances of tiles from their goal positions)