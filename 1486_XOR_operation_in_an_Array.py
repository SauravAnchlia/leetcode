class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ele_to_xor = [start + 2*i for i in range(0, n)]
        res = 0
        for index in range(0, len(ele_to_xor)):
            res ^= ele_to_xor[index]
        return res
