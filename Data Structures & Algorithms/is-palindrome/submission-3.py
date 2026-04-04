class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters, make lowercase
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        # Compare with reverse
        return cleaned == cleaned[::-1]
