class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(len(s)//2):
            temp = None
            if s[i]!=s[n-1-i]:
                temp = s[i]
                s[i] = s[n-1-i]
                s[n-1-i] = temp
        return s
        