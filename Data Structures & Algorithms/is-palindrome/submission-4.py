class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = [ ch.upper() for ch in s if ch.isalnum()]
        return result[::]==result[::-1]