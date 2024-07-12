# Daily DSA 


This repository contains solutions to various LeetCode problems implemented in Python. Below is a list of the problems tackled each day including a brief description and the corresponding LeetCode problem number.


## Problems Solved - Day 1


1. **Container with Most Water (LC 11)**
   - **Description**: Given an array of heights representing vertical lines, find two lines that together with the x-axis form a container that holds the most water.
   - **Solution**: Utilized a two-pointer approach to maximize the area between lines.


2. **Contains Duplicate (LC 217)**
   - **Description**: Given an integer array, determine if any value appears at least twice.
   - **Solution**: Employed a set to track duplicates efficiently.


3. **Group Anagrams (LC 49)**
   - **Description**: Given an array of strings, group the anagrams together.
   - **Solution**: Used a dictionary to categorize strings by their sorted character sequences.


4. **Longest Consecutive Sequence (LC 128)**
   - **Description**: Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
   - **Solution**: Implemented a set for efficient lookup and tracking of sequences.


5. **Product of Array Except Self (LC 238)**
   - **Description**: Given an array, return an array output such that output[i] is equal to the product of all the elements of the input array except nums[i].
   - **Solution**: Used prefix and suffix product arrays to achieve the solution without division.


6. **Three Sum (LC 15)**
   - **Description**: Given an integer array, find all the triplets that sum to zero.
   - **Solution**: Applied a two-pointer technique after sorting the array to find triplets efficiently.


7. **Top K Frequent Elements (LC 347)**
   - **Description**: Given a non-empty array of integers, return the k most frequent elements.
   - **Solution**: Utilized a frequency map and bucket sort to identify the top k elements.


8. **Two Sum (LC 1)**
   - **Description**: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
   - **Solution**: Used a hashmap to store and lookup complement values efficiently.


9. **Valid Anagram (LC 242)**
   - **Description**: Given two strings, determine if they are anagrams of each other.
   - **Solution**: Counted character frequencies using a dictionary for comparison.


10. **Valid Palindrome (LC 125)**
    - **Description**: Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring case.
    - **Solution**: Implemented two-pointer technique to compare characters from both ends.


## Getting Started


### Prerequisites


- Python 3.x
- Basic understanding of data structures and algorithms


### Running the Code


1. Clone the repository:
   ```bash
   git clone https://github.com/agnee008/daily_dsa_python.git
   cd daily_dsa_python
   ```


2. Run the desired Python file:
   ```bash
   python <filename>.py
   ```


### Example Usage


```python
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(twoSum(nums, 5))  # Example usage for Two Sum
```


## Contributing


If you have any improvements or suggestions for the code, feel free to open an issue or submit a pull request.


## License


This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
