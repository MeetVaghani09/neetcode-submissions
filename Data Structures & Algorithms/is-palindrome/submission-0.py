class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalnum():           # keep only letters and digits
                clean += ch.lower()    # ignore capitals
        return clean == clean[::-1]
