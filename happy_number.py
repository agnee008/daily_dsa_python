"""

Input: n = 19
Output: true
Explanation: 
19 is a happy number because:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Approach:
Sum of Squares Function:
Compute the sum of the squares of the digits of a number.
Floyd's Cycle Detection Algorithm:
Use two pointers, one moving fast (the hare) and one moving slow (the tortoise), to detect cycles.
If the hare and tortoise meet at any point other than 1, then there is a cycle and the number is not happy.


"""

def isHappy(n: int) -> bool:
    def sum_of_squares(num: int) -> int:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    slow = n
    fast = sum_of_squares(n)

    # Use Floyd's cycle detection algorithm
    while fast != 1 and slow != fast:
        slow = sum_of_squares(slow)
        fast = sum_of_squares(sum_of_squares(fast))
    
    return fast == 1

# Example usage:
print(isHappy(19))  # Output: True
print(isHappy(2))   # Output: False
