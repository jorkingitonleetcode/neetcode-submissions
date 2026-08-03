class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set()
        size = 0
        min_val = nums[0]
        current_max = 0


        for i in nums:
            min_val = min(i, min_val)
            if i not in set_nums:
                # check if previous is in
                set_nums.add(i)
                size += 1


        count = 0
        for i in range(min_val, min_val + size):
            if i in set_nums:
                count += 1
            else:
                count = 0
            current_max = max(current_max, count)

        return current_max