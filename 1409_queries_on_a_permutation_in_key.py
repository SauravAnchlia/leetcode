from typing import List

"""

Given the array queries of positive integers between 1 and m,
you have to process all queries[i] (from i=0 to i=queries.length-1)
according to the following rules:

In the beginning, you have the permutation P=[1,2,3,...,m].
For the current i, find the position of queries[i] in the permutation P
(indexing from 0) and then move this at the beginning of the
permutation P. Notice that the position of queries[i] in P
is the result for queries[i].
Return an array containing the result for the given queries.

Example :
Input: queries = [3,1,2,1], m = 5
Output: [2,1,2,1]
Explanation: The queries are processed as follow:

For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 2,
then we move 3 to the beginning of P resulting in P=[3,1,2,4,5].

For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 1,
then we move 1 to the beginning of P resulting in P=[1,3,2,4,5].

For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 2,
then we move 2 to the beginning of P resulting in P=[2,1,3,4,5].

For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 1,
then we move 1 to the beginning of P resulting in P=[1,2,3,4,5].
Therefore, the array containing the result is [2,1,2,1].

Link : https://leetcode.com/problems/queries-on-a-permutation-with-key/

"""


'''
Naive  approach
There are three things you need to know:
1. Find index by element
2. Delete by index  <list>.pop(index_position)
3. Insert by index  <list>.insert(position,element)

but list is the incorrect DS to use in python because it is not optimized for
multiple insertions and deletions.
Lists are not optimized for modifications at the front,
and somelist.insert(0, something) is an O(n) operation.
All of the above mentioned approaches are O(n)

python tip  :
Check out itertools count instead of using List.index
since list.index returns first occurance only
'''


class solution():
    def process_queries(self, queries: List[int], m: int) -> List[int]:
        permutation = [element for element in range(1, m+1)]
        sol = []
        for index in range(0, len(queries)):
            value = queries[index]
            ele = permutation.index(value)
            sol.append(ele)
            permutation.pop(ele)
            permutation.insert(0, value)
        return sol


obj = solution()
# print(obj.process_queries([3, 1, 2, 1], 5))
# print(obj.process_queries([4, 1, 2, 2], 4))
print(obj.process_queries([7, 5, 5, 8, 3], 8))


'''

https://cp-algorithms.com/data_structures/fenwick.html

'''
