class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = [num**2 for num in nums]
        new_nums = sorted(new_nums)
        return new_nums