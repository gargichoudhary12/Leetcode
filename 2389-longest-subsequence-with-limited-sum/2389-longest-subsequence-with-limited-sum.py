class Solution:
	def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
		result = []
		nums = sorted(nums)
		for i in range(len(queries)):
			current_sum = 0
			count = 0
			for j in range(len(nums)):
				current_sum+=nums[j]
				if current_sum <= queries[i]:
					count+=1
				else:
					break
			result.append(count)
		return result