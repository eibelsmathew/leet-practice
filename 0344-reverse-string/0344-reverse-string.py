class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(len(s)//2):
            if s[i]!=s[n-1-i]:
                s[i],s[n-1-i] = s[n-1-i], s[i]
        return s
        