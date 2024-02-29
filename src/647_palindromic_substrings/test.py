#!/usr/bin/python3

class countSubstrings:
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

	def solution(self, s: str) -> int:
		len_s = len(s)
		if len_s < 1 or len_s > 1000:
			return 1
		elif len_s == 1:
			print('The substring of count is 1.')
			return 0

		count = 0
		result = []
		# print(f'All cases: {self.sliding_window(s)}')
		for word in self.sliding_window(s):
			if len(word) == 1:
				count += 1
				result.append(word)
				continue

			len_w = len(word)
			avg_w = int(len_w / 2)

			if len_w % 2 == 0:
				if word[0:avg_w] == word[-1:avg_w-1:-1]:
					count += 1
					result.append(word)
			else:
				if word[0:avg_w] == word[-1:avg_w:-1]:
					count += 1
					result.append(word)

		print(f'The substring of count is {count}.')
		print(result)


a = countSubstrings()
a.solution('banana')
