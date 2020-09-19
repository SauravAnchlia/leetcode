from collections import Counter 

#sliding window 

class Solution:
    def minWindow(self, source: str, t: str) -> str:
        target_elements  = Counter(t)
        slow = 0
        min_slow, min_fast = float('-inf'), float('inf')
        missing = len(t)        
        for fast, element in enumerate(source):
            if target_elements[element] > 0:
                missing -= 1
            target_elements[element] -= 1

            while missing == 0:
                if fast - slow < min_fast - min_slow :
                    min_fast = fast
                    min_slow = slow 
                target_elements[source[slow]] += 1
                if target_elements[source[slow]] > 0:
                    missing += 1
                slow += 1

        
        if min_slow == float('inf'):
            return ""
        else:
            return source[min_slow: min_fast + 1]

obj = Solution()
print(obj.minWindow('aa','a'))
print(obj.minWindow('ab','a'))
print(obj.minWindow("ADOBECODEBANC","ABC"))
print(obj.minWindow('bba','ba'))
