from typing import List

class Solution:
    def pascalTriangleRow(self, rowNo: int) -> List[int]:
        if rowNo == 0:
            return [1]

        # Start with the first row
        row = [1]
        
        for _ in range(1, rowNo + 1):
            # Generate the next row using the current row
            new_row = [1]  # Start with 1
            for i in range(1, len(row)):
                new_row.append(row[i - 1] + row[i])
            new_row.append(1)  # End with 1
            row = new_row
        
        return row

# Example usage:
solution = Solution()
n = 5
print(solution.pascalTriangleRow(n))
