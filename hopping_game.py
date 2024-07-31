def simulate_game(arrayA, arrayB):
    visitedA = set()
    visitedB = []
    
    # Start at the first index of arrayA (0-based index 0)
    current_pos_a = 0
    
    while True:
        # If current position in arrayA has been visited, terminate
        if current_pos_a in visitedA:
            break
        
        # Mark the current position in arrayA as visited
        visitedA.add(current_pos_a)
        
        # Jump to the index in arrayB specified by arrayA[current_pos_a]
        current_pos_b = arrayA[current_pos_a] - 1  # Convert to 0-based index
        visitedB.append(current_pos_b + 1)  # Store the 1-based index
        
        # Jump to the index in arrayA specified by arrayB[current_pos_b]
        current_pos_a = arrayB[current_pos_b] - 1  # Convert to 0-based index

    return visitedB

# Example usage:
arrayA = [1, 3, 2, 5, 4]
arrayB = [5, 4, 3, 2, 1]
print(simulate_game(arrayA, arrayB))  # Output should be [1, 4, 3, 2, 5]
