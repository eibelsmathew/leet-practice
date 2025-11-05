class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_str = str(int("".join(map(str, digits))) + 1)
        res = [int(i) for i in new_str]
        return res
        
