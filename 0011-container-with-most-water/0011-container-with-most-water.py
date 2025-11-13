class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        maxarea = float(-inf)

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            maxarea = max(maxarea, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxarea
