from collections import defaultdict
from typing import List


class solution:
    def sort_by_bits(self, arr: List[int]) -> List[int]:
        number_of_1_hash = defaultdict(list)
        for number in arr:
            count = f'{number:b}'.count('1')
            number_of_1_hash[count].append(number)
        solution = []
        for values in number_of_1_hash.values():
            temp = []
            for number in values:
                temp.append(number)
            solution.extend(sorted(temp))
        return solution


obj = solution()
#obj.sort_by_bits([1, 3, 5, 7])
print(obj.sort_by_bits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
