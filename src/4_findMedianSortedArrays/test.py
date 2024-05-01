#!/usr/bin/python3


class Solution:
	def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
		offset = 0
		len1 = len(nums1)
		len2 = len(nums2)
		total_len = len1 + len2

		result = [0] * total_len
		i = 0
		j = 0
		k = 0
		for _ in range(total_len):
			# print(f'i={i}; len1={len1}; j={j}; len2={len2}; k={k}')
			if j == len1:
				result[i] = nums2[k]
				k += 1
			elif k == len2:
				result[i] = nums1[j]
				j += 1
			elif nums1[j] <= nums2[k]:
				result[i] = nums1[j]
				j += 1
			elif nums2[k] <= nums1[j]:
				result[i] = nums2[k]
				k += 1
			
			i += 1

		mid_idx = int(total_len / 2)
		if total_len % 2 == 0:
			ans = (result[mid_idx] + result[mid_idx - 1])/2
		else:
			ans = result[mid_idx]

		return ans

ans = Solution()
ans.findMedianSortedArrays([1,3], [2])
ans.findMedianSortedArrays([1,2], [3,4])

