from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # can I guess the topics?
        # array hash table union find
        # 100 4 1 3 2
        # 4: 1
        # 1: 1
        # 3: longest subsequence at 2 should grow by 1 and whatever length of subsequence at 4
        # 
        longest_sequence_at_num = defaultdict(int)
        max_len = 0
        for num in nums:
            if longest_sequence_at_num[num]:
                continue

            longest_sequence_at_num[num] = longest_sequence_at_num[num-1] + longest_sequence_at_num[num+1] + 1
            longest_sequence_at_num[num-longest_sequence_at_num[num-1]] = longest_sequence_at_num[num]
            longest_sequence_at_num[num+longest_sequence_at_num[num+1]] = longest_sequence_at_num[num]
            max_len = max(max_len, longest_sequence_at_num[num])
        return max_len