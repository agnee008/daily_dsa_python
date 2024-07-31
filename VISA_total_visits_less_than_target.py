from itertools import combinations

def count_valid_combinations(visits, target):
    # Check if the total sum of visits equals the target
    if sum(visits) != target:
        return -1
    
    valid_combinations_count = 0
    n = len(visits)
    
    # Check all possible combinations of visits
    for r in range(1, n + 1):
        for comb in combinations(visits, r):
            if sum(comb) < target:
                valid_combinations_count += 1
    
    # Return the count of valid combinations
    return valid_combinations_count

# Example usage
visits = [30, 40, 50]
target = 120

count = count_valid_combinations(visits, target)
print(count)
