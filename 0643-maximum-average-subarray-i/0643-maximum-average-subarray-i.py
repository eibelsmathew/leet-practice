class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w_sum = 0
        start = 0
        max_avg = float(-inf)
        for avg in range(len(nums)):
            w_sum += nums[avg]
            if avg >= k - 1:
                max_avg = max(max_avg, w_sum/k)
                w_sum -= nums[start]  
                start += 1 
            
        return max_avg
