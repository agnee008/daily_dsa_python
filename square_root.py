class Solution:
    def sqrt(self, n: int) -> int:
        if n < 0:
            raise ValueError("Cannot compute the square root of a negative number.")
        if n == 0:
            return 0
        if n == 1:
            return 1

        left, right = 1, n
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == n:
                return mid
            elif mid * mid < n:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result

# Example usage:
solution = Solution()
print(solution.sqrt(16))  # Output should be 4
print(solution.sqrt(12))  # Output should be 3
print(solution.sqrt(0))   # Output should be 0
