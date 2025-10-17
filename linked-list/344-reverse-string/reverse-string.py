class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(int(len(s)/2)):
            s[i], s[n-1] = s[n-1], s[i]
            n = n-1
        return s
        