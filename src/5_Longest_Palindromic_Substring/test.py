#!/usr/bin/python3


class Solution():
	def longestPalindrome(self, s: str) -> str:
		len_s = len(s)

		for i in range(len_s, 0, -1):  # window size
			for j in range(len_s):  # Start index
				end_idx = j + i + 1
				if end_idx > len_s:
					continue

				word = s[j:end_idx]
				reverse_w = word[::-1]
				if word == reverse_w:
					return word

		return s[0]


# a = Solution()
# print(a.longestPalindrome('apple'))
# print(a.longestPalindrome('ac'))
# print(a.longestPalindrome('appkoasdseeeeeedeeeee'))
