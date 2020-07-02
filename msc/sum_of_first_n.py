class solution():
    def sum_of_n(self, n: int):
        total = []
        total.append(0)
        print(total)
        for index in range(1, n+1):
            total.append(total[index-1] + index)
        return total[n]


obj = solution()
print(obj.sum_of_n(5))
