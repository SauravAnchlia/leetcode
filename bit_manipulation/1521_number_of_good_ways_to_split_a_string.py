from collections import Counter
from collections import defaultdict


'''
You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.

Return the number of good splits you can make in s.
'''

# difficulty : medium
# topic : bit manipulation
# link : https://leetcode.com/problems/number-of-good-ways-to-split-a-string/


class Solution:
    def num_splits(self, s: str) -> int:
        pre_combination = []
        post_combination = []
        pre = defaultdict(int)
        post = defaultdict(int)
        for index, item in enumerate(s):
            pre[item] += 1 
            post[s[len(s) - 1 - index]] += 1
            pre_combination[index] = len(pre.keys())
            post_combination[len(s) - 1 - index] = len(post.keys())
        good = 0
        for item in range(0,len(s)):
            if pre_combination[item] == post_combination[len(s) - 1 -item]:
                good += 1
        return good 
    def num_splits_dict(self, s: str) -> int:
        counts = Counter(s)
        unique = len(counts.keys())
        seen = defaultdict(int)
        current = len(seen.keys())
        good = 0
        for item in s:
            seen[item] += 1
            current = len(seen.keys())
            counts[item] -= 1
            if counts[item] == 0:
                unique -= 1
            if unique == current:
                good += 1
        return good 