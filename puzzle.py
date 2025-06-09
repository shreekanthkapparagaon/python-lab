def count_inversions(state): 
    tiles = [tile for tile in state if tile != 0] 
    inversions = 0 
    for i in range(len(tiles)): 
        for j in range(i + 1, len(tiles)): 
            if tiles[i] > tiles[j]: 
                inversions += 1 
    return inversions 
def puzzle_parity(state): 
    inversions = count_inversions(state) 
    return inversions % 2 
state_1 = [1, 2, 3, 4, 5, 6, 7, 8, 0] 
state_2 = [1, 2, 3, 4, 5, 6, 0, 8, 7] 
print(f"State 1 parity: {puzzle_parity(state_1)} (Even set)") 
print(f"State 2 parity: {puzzle_parity(state_2)} (Odd set)") 
if puzzle_parity(state_1) == puzzle_parity(state_2): 
    print("Both states are in the same set.") 
else: 
    print("The states are in different sets.") 