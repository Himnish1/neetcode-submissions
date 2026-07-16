class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # whenever order matters, and contiguous sequence is needed
        # sliding window makes sense
        # zxyzxyz
        left = None
        right = None
        seen = dict()
        max_substring = 0
        if s == "":
            return 0
        for i, char in enumerate(s):
            print(f"{char=}", f"{left=}", f"{right=}", f"{seen=}")
            if left is None:
                left = i
                seen[char] = i
                max_substring = 1
            else:
                # left is set, right isn't
                if char in seen.keys():
                    # move left to char right after duplicate
                    left = max(seen[char] + 1, left+1)
                    seen[char] = i
                    seen = {char: index for char, index in seen.items() if index >= left}
                    right = i
                    max_substring = max(max_substring, right-left+1)
                else:
                    right = i
                    seen[char] = i
                    max_substring = max(max_substring, right-left+1)

        return max_substring
            