#!/usr/bin/python3

class Solution:
	def three_sum(self, nums: list) -> list:
		result = []
		len_nums = len(nums)

		if len_nums == 3:
			if sum(nums) == 0:
				return nums
			else:
				return []

		for i in range(len_nums):
			for j in range(i+1, len_nums):
				if i == j:					
					continue
				for k in range(i+2, len_nums):
					if i == k or j == k:
						continue

					ans = nums[i] + nums[j] + nums[k]
					if ans == 0:
						return [nums[i], nums[j], nums[k]]

ans = Solution()
print(ans.three_sum([-1,0,1,2,-1,-4]))
print(ans.three_sum([0,1,1]))
print(ans.three_sum([0,0,0]))
print(ans.three_sum([-1,0,3,2,-1,-4]))
print(ans.three_sum([1,2,3,2,-1,-4]))