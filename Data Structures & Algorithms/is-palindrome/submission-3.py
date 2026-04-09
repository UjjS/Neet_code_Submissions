class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(ch.upper() for ch in s if ch.isalnum())
        return result[::]==result[::-1]