class solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while(x or y):
            if x & 1 == y & 1:
                next
            else:
                count += 1
            x >>= 1
            y >>= 1

        return count


obj = solution()
print(obj.hammingDistance(4, 1))
