class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        out=[]
        word1 = s1.split()
        word2 = s2.split()
        for i in word1:
            if i not in word2:
                if word1.count(i)<2:
                    out.append(i)
        for i in word2:
            if i not in word1:
                if word2.count(i)<2:
                    out.append(i)
        return out