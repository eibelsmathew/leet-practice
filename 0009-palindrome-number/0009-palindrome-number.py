class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = str(x)
        new_rev = rev[::-1]
        if rev == new_rev:
            return True
        else:
            return False