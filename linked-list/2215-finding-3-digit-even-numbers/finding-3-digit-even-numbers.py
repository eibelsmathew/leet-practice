class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        leng = len(digits)
        res = []
        numb = 0

        for i in range(0, leng):
            if digits[i] == 0:
                continue
            for j in range(0, leng):
                if j == i:
                    continue
                for k in range(0, leng):
                    if k == j or k == i or digits[k] % 2 != 0:
                        continue
    
                    numb = digits[i] * 100 + digits[j] * 10 + digits[k]
                    res.append(numb)
        
        return sorted(list(set(res)))
                    