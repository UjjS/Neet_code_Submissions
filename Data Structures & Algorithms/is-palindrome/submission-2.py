class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(ch.upper() for ch in s if ch.isalnum())
        for i in range(len(result)//2):
            if result[i]!=result[len(result)-i-1]:
                return False 
        return True