class Solution:
    def maxScore(self, nums: List[int]) -> int:
        num_elems = len(nums)
        gcd_pairs = [[gcd(nums[i], nums[j]) for j in range(num_elems)] for i in range(num_elems)]
        max_scores = [0] * (1 << num_elems)
        for state in range(1, 1 << num_elems):
            num_selected = bin(state).count('1')
            if num_selected % 2 == 1:
                continue
            for i in range(num_elems):
                if not (state & (1 << i)):
                    continue
                for j in range(i+1, num_elems):
                    if not (state & (1 << j)):
                        continue
                    prev_state = state ^ (1 << i) ^ (1 << j)
                    current_score = max_scores[prev_state] + num_selected // 2 * gcd_pairs[i][j]
                    max_scores[state] = max(max_scores[state], current_score)
        return max_scores[(1 << num_elems) - 1]