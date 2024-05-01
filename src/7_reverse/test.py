#!/usr/bin/python3

class Solution:
	def reverse(self, x: int) -> int:
		str_num = str(abs(x))
		result = int(str_num[::-1])

		if result <= -(2**31) or result >= 2**31 -1:
			return 0

		if x >= 0:
			return result
		else:
			return -result



# a = Solution()
# print(a.reverse(123))
# print(test(-2147483412))