class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for n in num_set:
            if (n-1) not in num_set:
                curr_n = n
                curr_len = 1
                while (curr_n + 1) in num_set:
                    curr_n += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len

                 

        

