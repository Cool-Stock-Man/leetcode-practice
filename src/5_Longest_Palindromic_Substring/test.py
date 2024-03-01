#!/usr/bin/python3

class Solution:
	def sliding_window(self, word: str) -> list:
		result = []
		for w_size in range(1, len(word) + 1):
			sliding_times = len(word) - w_size + 1
			for i in range(0, sliding_times):
				end_idx = i + w_size
				if end_idx == i:
					continue

				result.append(word[i:end_idx])

		return result

	def longestPalindrome(self, s: str) -> int:
		len_s = len(s)
		if len_s < 1 or len_s > 1000:
			return 1
		elif len_s == 1:
			print(s)
			return 0

		max_len = 0
		result = ''
		for word in self.sliding_window(s):
			len_w = len(word)
			if len_w == 1 and len_w > max_len:
				result = word
				max_len = 1
				continue

			avg_w = int(len_w / 2)

			if len_w % 2 == 0:
				if word[0:avg_w] == word[-1:avg_w-1:-1] and \
					len_w > max_len:
					result = word
					max_len = len_w
			else:
				if word[0:avg_w] == word[-1:avg_w:-1] and \
					len_w > max_len:
					result = word
					max_len = len_w

		print(result)


a = Solution()
a.longestPalindrome('banana')
a.longestPalindrome('apple')