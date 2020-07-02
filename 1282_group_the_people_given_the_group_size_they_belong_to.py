from typing import List
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        organizer = defaultdict(list)
        answer = []
        for id, group in enumerate(groupSizes):
            if len(organizer[group]) != group:
                organizer[group].append(id)
            else:
                answer.append(organizer[group])
                organizer.pop(group)
                organizer[group].append(id)
        for key, val in organizer.items():
            answer.append(val)
        return answer


obj = Solution()
print(obj.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
