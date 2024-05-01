#!/usr/bin/python3


class Solution:
	def convert(self, s: str, numRows: int) -> str:
		mid = numRows - 2
		d = numRows + mid

		if len(s) <= numRows:
			for alphabet in s:
				print(alphabet)

			print('\n')
			return 0

		count = 0
		result = []
		for _ in range(numRows):
			result.append('')
		for alphabet in s:
			i = count % d
			if i < numRows:
				result[i] += alphabet
			elif i < d:
				for j in range(numRows):
					if j == (numRows - 2 - (i - numRows)):
						result[j] += alphabet
					else:
						result[j] += ' '
			count += 1

		for ans in result:
			print(ans)
		print('\n')


ans = Solution()
ans.convert(s='PAYPALISHIRING', numRows=3)
ans.convert(s='PAYPALISHIRING', numRows=4)
ans.convert(s='A', numRows=1)
ans.convert(s='THINKPAD', numRows=4)
