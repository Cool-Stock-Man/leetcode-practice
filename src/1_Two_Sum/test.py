#!/usr/bin/python3

class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		for i in range(len(nums)):
			for j in range(len(nums)):
				if i == j:
					continue

				num1 = nums[i]
				num2 = target - num1

				if nums[j] == num2:
					return [i, j]

		return None

# ans = Solution()
# ans.twoSum([1, 3, 5, 2, 8, 6], 9)
# ans.twoSum([3, 2, 3], 6)
