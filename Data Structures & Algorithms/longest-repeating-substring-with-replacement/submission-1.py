from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # contiguous property is max same character plus k others
        # keep a hashmap of letters at most 26 characters long
        # maintain a sliding window that helps you udate the hashmap
        left = 0
        right = 0
        hashmap = defaultdict(int)
        max_len = 0

        while right < len(s):
            hashmap[s[right]] += 1
            # check condition, what's most frequent char
            max_frequency = 0
            max_key = None
            for key, frequency in hashmap.items():
                if frequency > max_frequency:
                    max_key = key
                    max_frequency = frequency

            len_substring = right - left + 1
            while len_substring - max_frequency > k:
                # we need to move sliding window
                hashmap[s[left]] -= 1
                max_frequency = 0
                max_key = None
                for key, frequency in hashmap.items():
                    if frequency > max_frequency:
                        max_key = key
                        max_frequency = frequency
                left += 1
                len_substring -= 1

            # we good, proceed right
            right += 1
            max_len = max(len_substring, max_len)
        return max(len_substring, max_len)




       



                

