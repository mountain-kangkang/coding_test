from collections import deque
import copy
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        right = deque()

        while queue:
            strings = copy.deepcopy(queue)
            for st in strings:
                if st == "R" and "D" in right:
                    right.popleft()
                    queue.popleft()
                    continue
                elif st == "D" and "R" in right:
                    right.popleft()
                    queue.popleft()
                    continue
                queue.append(queue.popleft())
                right.append(st)
            if "R" not in queue:
                return "Dire"
            elif "D" not in queue:
                return "Radiant"
