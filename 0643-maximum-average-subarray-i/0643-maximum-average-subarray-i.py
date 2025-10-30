class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        average = window_sum/k

        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i-k]

            average = max(average, window_sum/k)
        return average