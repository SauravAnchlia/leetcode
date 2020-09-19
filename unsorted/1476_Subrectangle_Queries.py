from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int,
                           newValue: int) -> None:
        print(self.rectangle)
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                print(f'R {r} and C {c}')
                self.rectangle[r][c] = newValue
        return self.rectangle

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


rectangle = [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
obj = SubrectangleQueries(rectangle)
print(obj.updateSubrectangle(0, 0, 3, 2, 5))
param_2 = obj.getValue(0, 2)
