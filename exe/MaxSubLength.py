from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # last = nums[dp.index(max(dp))]
        # sublist = []
        # for i in range(len(dp)):
        #     if nums[i] < last:
        #         sublist.append(nums[i])
        return max(dp)

solution = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
length = solution.lengthOfLIS(nums)
print(length)

