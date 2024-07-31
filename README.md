# Python Algorithms and Data Structures

This repository contains a collection of Python scripts implementing various algorithms and solving problems from LeetCode (indicated by `lc` in the filenames). The problems cover a wide range of topics, including dynamic programming, string manipulation, array operations, and more.

## Table of Contents

1. [Array and List Problems](#array-and-list-problems)
2. [Dynamic Programming](#dynamic-programming)
3. [String Manipulation](#string-manipulation)
4. [Mathematical Problems](#mathematical-problems)
5. [Other Problems](#other-problems)
6. [Conversion Scripts](#conversion-scripts)

## Array and List Problems

- `best_time_to_buy_and_sell_stock.py`: Solution for the "Best Time to Buy and Sell Stock" problem (lc). Uses dynamic programming to track the minimum price and maximum profit.
- `binary_search.py`: Implementation of the binary search algorithm. Efficiently searches for an element in a sorted array.
- `candies.py`: Distributing candies to children. Solves the problem using a greedy approach.
- `coin_change.py`: Solution for the "Coin Change" problem (lc). Uses dynamic programming to find the minimum number of coins needed to make up a given amount.
- `combination_sum.py`: Solution for the "Combination Sum" problem (lc). Uses backtracking to find all unique combinations that add up to a target sum.
- `container_with_max_water_leetcode_11.py`: Solution for the "Container With Most Water" problem (lc). Uses a two-pointer technique to find the maximum area.
- `contains_duplicate_leetcode_217.py`: Solution for the "Contains Duplicate" problem (lc). Uses a hash set to check for duplicates in linear time.
- `convert_array_to_zigzag.py`: Converting array to zigzag fashion. Uses a single scan to swap elements and achieve the zigzag pattern.
- `daily_temperatures.py`: Solving the "Daily Temperatures" problem (lc). Uses a stack to find the number of days until a warmer temperature.
- `hopping_game.py`: Solving the "Hopping Game" problem. Uses dynamic programming to determine if you can reach the last index.
- `intersection_of_two_arrays.py`: Finding the intersection of two arrays (lc). Uses hash sets to find common elements.
- `jump_game.py`: Solution for the "Jump Game" problem (lc). Uses greedy or dynamic programming to determine if you can reach the last index.
- `longest_consecutive_sequence_leetcode_128.py`: Solution for the "Longest Consecutive Sequence" problem (lc). Uses a hash set to find the longest sequence in linear time.
- `merge_sorted_list.py`: Merging two sorted lists. Uses two pointers to merge the lists in linear time.
- `missing_number_(all).py`: Solutions for finding the missing number in a sequence. Implements various methods including sum formula and XOR.
- `move_zeroes.py`: Solution for the "Move Zeroes" problem (lc). Uses a two-pointer technique to move all zeroes to the end while maintaining the order of non-zero elements.
- `plus_one.py`: Solution for the "Plus One" problem (lc). Handles the carry-over for incrementing the number represented by an array of digits.
- `product_of_array_except_self_leetcode_238.py`: Solution for the "Product of Array Except Self" problem (lc). Uses two arrays to store the product of elements to the left and right of each element.
- `rotate_array.py`: Solution for the "Rotate Array" problem (lc). Uses array reversal to rotate the array in place.
- `search_rotated_sorted_array_leetcode_33.py`: Solution for the "Search in Rotated Sorted Array" problem (lc). Uses modified binary search to account for rotation.
- `three_sum_leetcode_15.py`: Solution for the "3Sum" problem (lc). Uses sorting and a three-pointer technique to find all unique triplets that sum to zero.
- `top_k_frequent_elements_leetcode_347.py`: Solution for the "Top K Frequent Elements" problem (lc). Uses a heap to find the k most frequent elements.
- `two_sum_leetcode_1.py`: Solution for the "Two Sum" problem (lc). Uses a hash map to find two numbers that add up to a specific target in linear time.
- `count_pairs_with_given_sum.py`: Counting pairs with a given sum. Uses a hash map to count pairs efficiently.
- `frequency_sort.py`: Sorting elements by frequency. Uses a hash map and a heap to sort elements based on frequency.
- `maximum_product_subarray.py`: Finding the maximum product subarray (lc). Uses dynamic programming to track the maximum and minimum products.
- `maximum_subarray.py`: Finding the maximum subarray (lc). Uses Kadane's algorithm to find the maximum sum subarray in linear time.
- `merge_intervals.py`: Merging intervals (lc). Sorts intervals and then merges overlapping intervals.
- `replace_every_element_with_greatest_element_right_side.py`: Replace every element with the greatest element on its right side. Scans the array from right to left to track the greatest element.
- `unique_paths.py`: Finding the number of unique paths in a grid (lc). Uses dynamic programming to count paths from the top-left to the bottom-right corner.

## Dynamic Programming

- `fibonacci_series.py`: Generating Fibonacci series. Uses memoization to store previously computed values.
- `longest_common_subsequence.py`: Finding the longest common subsequence. Uses a 2D array to store lengths of longest common subsequences of substrings.
- `longest_commonprefix.py`: Finding the longest common prefix among strings (lc). Uses vertical scanning to find the common prefix.
- `longest_increasing_sequence.py`: Finding the longest increasing subsequence. Uses dynamic programming with a binary search for efficient calculation.
- `longest_palindromic_subsequence.py`: Finding the longest palindromic subsequence. Uses a 2D array to store lengths of palindromic subsequences.
- `longest_substring_without_repeat_leetcode_3.py`: Solution for the "Longest Substring Without Repeating Characters" problem (lc). Uses a sliding window and hash map to track characters and their positions.
- `min_moves_to_make_all_number_equal_array.py`: Minimum moves to make all numbers equal in an array. Uses the median to calculate the minimum number of moves.
- `climbing_stairs.py`: Solving the "Climbing Stairs" problem (lc). Uses dynamic programming to count the number of ways to reach the top.
- `decode_ways.py`: Solving the "Decode Ways" problem (lc). Uses dynamic programming to count the number of ways to decode a string.
- `hopping_game.py`: Solving the "Hopping Game" problem. Uses dynamic programming to determine if you can reach the last index.

## String Manipulation

- `find_non_repeat.py`: Finding the first non-repeating character in a string. Uses a hash map to count character frequencies and find the first unique character.
- `generate_paranthesis.py`: Generating valid parentheses combinations (lc). Uses backtracking to generate all combinations of well-formed parentheses.
- `group_anagram_leetcode_49.py`: Solution for the "Group Anagrams" problem (lc). Uses a hash map to group words by their sorted character sequences.
- `integer_to_roman.py`: Converting an integer to a Roman numeral. Uses a greedy algorithm to map integers to Roman numerals.
- `isomorphic_strings.py`: Checking if two strings are isomorphic (lc). Uses two hash maps to map characters from one string to another.
- `longest_palindromic_subsequence.py`: Finding the longest palindromic subsequence. Uses dynamic programming with a 2D array to store lengths of palindromic subsequences.
- `LRU_cache.py`: Implementation of an LRU Cache (lc). Uses a hash map and a doubly linked list to store cache keys and values with efficient access and eviction.
- `pascal_to_snake.py`: Converting PascalCase to snake_case. Uses regular expressions to convert string formats.
- `permutations_possible.py`: Checking if permutations are possible. Uses a hash map to count character frequencies and determine if a palindrome permutation is possible.
- `power_set.py`: Generating the power set. Uses backtracking to generate all subsets of a given set.
- `power_sum.py`: Calculating the power sum. Uses recursion to calculate the sum of powers of elements in a set.
- `roman_to_integer.py`: Converting a Roman numeral to an integer. Uses a hash map to map Roman numerals to integers and calculate the total.
- `snake_to_pascal.py`: Converting snake_case to PascalCase. Uses string manipulation to convert formats.
- `valid_anagram_leetcode_242.py`: Solution for the "Valid Anagram" problem (lc). Uses sorting or hash maps to determine if two strings are anagrams.
- `valid_palindrome_leetcode_125.py`: Solution for the "Valid Palindrome" problem (lc). Uses two pointers to check if a string reads the same forward and backward.
- `valid_paranthesis_leetcode_20.py`: Solution for the "Valid Parentheses" problem (lc). Uses a stack to ensure that parentheses are balanced.
- `run_length_encoding.py`: Run-length encoding. Compresses a string by storing the lengths of consecutive character runs.
- `analyze_user_website_visit_pattern.py`: Analyzing user website visit patterns (lc). Uses a hash map to count and rank patterns of website visits.
- `word_search.py`: Solving the "Word Search" problem (lc). Uses backtracking to find if a word exists in a grid.

## Mathematical Problems

- `find_factors.py`: Finding the factors of a given number. Uses a loop to find all divisors of a number.
- `power_set.py`: Generating the power set. Uses bit manipulation to generate all subsets of a set.
- `highest_power_of_2_less_than_equal_to.py`: Finding the highest power of 2 less than or equal to a given number. Uses bit manipulation to find the result.
- `square_root.py`: Calculating the square root. Uses binary search to find the square root of a number.
- `sum_of_two_numbers_without_operator.py`: Sum of two numbers without using operator. Uses bit manipulation to add numbers without the `+` operator.

## Other Problems

- `revision_1.py`: Miscellaneous revision problems. Includes a variety of problems for practice and review.
- `k_closest_point_to_origin.py`: Finding k closest points to origin (lc). Uses a heap to efficiently find the closest points.
- `max_depth_of_binary_tree.py`: Maximum depth of a binary tree (lc). Uses recursion to find the maximum depth of a binary tree.
- `max_product_pair.py`: Finding maximum product pair. Uses sorting or a linear scan to find the pair of elements with the maximum product.
- `number_of_islands.py`: Finding the number of islands (lc). Uses depth-first search (DFS) or breadth-first search (BFS) to count islands in a grid.
- `odd_even_sum_difference_binary_tree.py`: Finding the difference between odd and even level sums in a binary tree. Uses level-order traversal to calculate sums at odd and even levels.
- `pascal_triangle.py`: Generating Pascal's triangle (lc). Uses a loop to generate the rows of Pascal's triangle.
- `reverse_linked_list.py`: Reversing a linked list (lc). Uses iteration or recursion to reverse the links in a linked list.
- `search_in_row_and_column_sorted_matrix.py`: Searching in a row and column sorted matrix (lc). Uses a binary search-like approach to find an element in the matrix.
- `search_suggestion_system.py`: Implementing a search suggestion system (lc). Uses a trie or prefix tree to store and retrieve suggestions efficiently.
- `validate_bst.py`: Validating a binary search tree (lc). Uses in-order traversal to ensure the tree satisfies the BST properties.
- `VISA_inventory_tracking_system.py`: Tracking inventory for VISA system. Implements tracking features for an inventory system.
- `VISA_queries_integers.py`: Handling integer queries for VISA system. Solves problems related to integer operations.
- `VISA_round_trip_calculation.py`: Calculating round trip distances for VISA system. Implements logic for distance calculation.
- `VISA_total_visits_less_than_target.py`: Finding total visits less than target for VISA system. Implements logic to count visits below a certain threshold.

## Conversion Scripts

- `pascal_to_snake.py`: Converting PascalCase to snake_case. Uses regular expressions to convert string formats.
- `snake_to_pascal.py`: Converting snake_case to PascalCase. Uses string manipulation to convert formats.

## Usage

Each script can be run individually. For example, to run the `two_sum_leetcode_1.py` script, use the following command:

```bash
python two_sum_leetcode_1.py
