#!/usr/bin/python3

def twoSum(nums: list[int], target: int) -> list[int]:
	for i in range(len(nums)):
		plus_nums = nums
		plus_nums.pop(i)

		num1 = nums[i]
		num2 = target - num1
		
		if num2 in plus_nums:
			return [num1, num2]

print(twoSum([1, 3, 5, 2, 8, 6], 9))
