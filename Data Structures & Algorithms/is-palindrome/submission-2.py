class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = [i for i in s if i.isalnum()]
        for i in range(len(filtered_s)):
            if filtered_s[i].lower() != filtered_s[-(i+1)].lower():
                return False
            
            
        return True