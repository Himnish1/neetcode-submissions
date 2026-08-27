from collections import defaultdict
from copy import deepcopy 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = some letters
        # if s2 has letters contiguously in any order
        # {a: 1, b: 1, c: 1}
        # lecabee
        # left = c
        # right is c {a: 1, b: 1, c: 0}
        # right is b, b is in there with 1, {}
        checker = defaultdict(int)
        for char in s1:
            # count freq
            checker[char] += 1

        left = 0
        right = 0
        checker_copy = deepcopy(checker)

        while right < len(s2):
            if [key for key, value in checker_copy.items() if value > 0] == []:
                # done
                return True
            if checker_copy[s2[right]] > 0:
                # exists, decrement and move right
                checker_copy[s2[right]] -= 1
                right += 1
                continue
            else:
                left += 1
                right = left
                checker_copy = deepcopy(checker)
        if [key for key, value in checker_copy.items() if value > 0] == []:
            # done
            return True
        else:
            return False
