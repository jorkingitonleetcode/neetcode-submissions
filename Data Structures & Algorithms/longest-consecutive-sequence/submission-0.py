class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set()
        size = 0
        current_max = 0

        for i in nums:
            if i not in set_nums:
                # check if previous is in
                set_nums.add(i)
                size += 1


        count = 0
        for i in range(0, size):
            if i in set_nums:
                count += 1
            else:
                count = 0
            current_max = max(current_max, count)

        return current_max