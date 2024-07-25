from collections import defaultdict
from itertools import combinations
from typing import List

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        G = defaultdict(list)
        for (t, user, web) in sorted(zip(timestamp, username, website)):
            G[user].append(web)
        
        scores = defaultdict(int)
        for user, websites in G.items():
            # Generate all unique combinations of 3 websites the user visited
            for pattern in set(combinations(websites, 3)):
                scores[pattern] += 1
        
        max_pattern = ()
        max_cnt = 0
        for pattern, cnt in scores.items():
            # Find the pattern with the highest score, or lexicographically smallest if there is a tie
            if cnt > max_cnt or (cnt == max_cnt and pattern < max_pattern):
                max_pattern = pattern
                max_cnt = cnt
        
        return list(max_pattern)
