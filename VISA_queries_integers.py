"""
Given an empty array that should contain integers `numbers`, your task is to process a list of `queries`  on it. Specifically, there are two types of queries.

* "+x" - add integer `x` to `numbers`.`numbers` may contain multiple instances of the same integer. 
* "-x" - remove a single instance of integer `x` from `numbers`.


After processing each query, record the number of pairs in `numbers` with a difference equal to a given `diff`. The final output should be an array of such values for all `queries`.


Example
* For `queries = ["+4", "+5", "+2", "-4"]` and `diff = 1`, the output should be `solution(queries, diff) = [0,1,1,0]

"""

def solution(queries, diff):
    from collections import defaultdict
    
    count = defaultdict(int)
    pair_count = 0
    result = []
    
    for query in queries:
        operation = query[0]
        x = int(query[1:])
        
        if operation == '+':
            # Add x to the count
            count[x] += 1
            
            # Update pair_count
            if diff != 0:
                pair_count += count[x - diff]  # pairs (x-diff, x)
                pair_count += count[x + diff]  # pairs (x, x+diff)
            else:
                pair_count += count[x] - 1  # pairs (x, x)
        
        elif operation == '-':
            # Remove x from the count if it exists
            if count[x] > 0:
                # Update pair_count
                if diff != 0:
                    pair_count -= count[x - diff]  # pairs (x-diff, x)
                    pair_count -= count[x + diff]  # pairs (x, x+diff)
                else:
                    pair_count -= count[x] - 1  # pairs (x, x)
                
                count[x] -= 1
        
        # Record the current number of pairs
        result.append(pair_count)
    
    return result

# Example usage
queries = ["+4", "+5", "+2", "-4"]
diff = 1
print(solution(queries, diff))  # Output: [0, 1, 1, 0]
