from collections import defaultdict


class solution():
    def recursion(self, t1: str, t2: str, index: int, jindex: int) -> int:
        # import pdb; pdb.set_trace()
        if index >= len(t1) or jindex >= len(t2):
            print(f' if {index} and jindex {jindex}')
            return 0
        elif t1[index] == t2[jindex]:
            print(f'same {index} and {jindex}')
            return (1 + self.recursion(t1, t2, index+1, jindex+1))
        else:
            x = self.recursion(t1, t2, index+1, jindex)
            y = self.recursion(t1, t2, index, jindex+1)
            print(f' index {index} and jindex {jindex}')
            print(f'x is {x} y is {y}')
            return (max(self.recursion(t1, t2, index+1, jindex),
                    self.recursion(t1, t2, index, jindex+1)))

    def lcs(self, text1: str, text2: str):
        l_t1 = len(text1)
        l_t2 = len(text2)

        lookup = [[0 for jindex in range(l_t2 + 1)] for index in range(l_t1 + 1)]
        print(lookup)
        for index in range(l_t1 + 1):
            for jindex in range(l_t2 + 1):
                if index == 0 or jindex == 0:
                    lookup[index][jindex] = 0
                elif text1[index - 1] == text2[jindex - 1]:
                    lookup[index][jindex] = lookup[index - 1][jindex - 1] + 1
                else:
                    lookup[index][jindex] = max(lookup[index - 1][jindex],
                                                lookup[index][jindex - 1])

        return lookup[l_t1][l_t2]


obj = solution()
print(obj.lcs('abcde', 'bd'))
