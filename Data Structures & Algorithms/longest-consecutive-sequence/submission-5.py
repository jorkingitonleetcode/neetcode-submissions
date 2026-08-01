class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set()
        size = 0
        if len(nums) > 0:
            min_val = nums[0] 
            max_val = nums[0]
        else:
            return 0
        current_max = 0


        for i in nums:
            min_val = min(i, min_val)
            max_val = max(i, max_val)
            if i not in set_nums:
                # check if previous is in
                set_nums.add(i)
                size += 1


        count = 0
        for i in range(min_val, max_val + 1):
            if i in set_nums:
                count += 1
            else:
                count = 0
            current_max = max(current_max, count)

        return current_max