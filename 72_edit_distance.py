class Solution:
    def recursive(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)

    def dp_bottom_up(self, word1: str, word2: str):

        l_w1 = len(word1)
        l_w2 = len(word2)

        lookup = [[0 for jindex in range(l_w2 + 1)] for index in range(l_w1 + 1) ]

        for jindex in range(l_w2 + 1):
            lookup[0][jindex] = jindex
        for index in range(l_w1 + 1):
            lookup[index][0] = index

        for index in range(1, l_w1 + 1):
            for jindex in range(1, l_w2 + 1):
                if word1[index - 1] == word2[jindex - 1]:
                    lookup[index][jindex] = lookup[index - 1][jindex - 1]
                else:
                    lookup[index][jindex] = 1 + min(lookup[index - 1][jindex],
                                                    lookup[index][jindex - 1],
                                                    lookup[index - 1][jindex - 1])
        print(lookup)
        return lookup[l_w1][l_w2]


obj = Solution()
# min = obj.minDistance("horse", "ros")
min = obj.dp_bottom_up("", "a")
print(min)
