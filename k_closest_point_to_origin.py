"""
Why Use a Heap?

1.Efficiency for Large Datasets:

When you only need the K closest points out of a large dataset, a heap can help reduce the time complexity compared to sorting the entire dataset.
Building a min-heap (or max-heap, depending on the implementation) from the points can be done in 
O(nlogK) time,  whereas sorting all points requires O(nlogn) time

2.Incremental Extraction:

With a heap, you can efficiently maintain the K smallest elements seen so far. This means you don't need to sort the entire list, just ensure the heap size doesn't exceed K.
This incremental nature of heaps is useful when dealing with streaming data or when the entire dataset cannot be loaded into memory at once.
"""


import heapq
from typing import List, Tuple

def kClosest(points: List[Tuple[int, int]], K: int) -> List[Tuple[int, int]]:
    # Calculate the Euclidean distance squared for each point
    def euclidean_distance(point):
        x, y = point
        return x * x + y * y

    # Create a min-heap of points based on their distance to the origin
    heap = [(euclidean_distance(point), point) for point in points]
    heapq.heapify(heap)

    # Extract the K closest points
    closest_points = [heapq.heappop(heap)[1] for _ in range(K)]
    
    return closest_points

# Example usage:
points = [(1, 3), (3, 4), (2, -1)]
K = 2
result = kClosest(points, K)
print(result)  # Output: [(1, 3), (2, -1)]


"""
Alternatively, you can solve this problem by sorting the points based on their distance to the origin and then selecting the first K points:
"""

def kClosest(points: List[Tuple[int, int]], K: int) -> List[Tuple[int, int]]:
    points.sort(key=lambda point: point[0]**2 + point[1]**2)
    return points[:K]

# Example usage:
points = [(1, 3), (3, 4), (2, -1)]
K = 2
result = kClosest(points, K)
print(result)  # Output: [(1, 3), (2, -1)]
