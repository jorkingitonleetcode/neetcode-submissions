class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1 = 0
        ptr2 = 1
        max_area = 0
        while(ptr1 < len(heights) and ptr2 < len(heights)):
            max_area = max(max_area, abs(ptr1 - ptr2)  * min(heights[ptr1], heights[ptr2]))
            if heights[ptr1] == heights[ptr2]:
                # whichever is larger
                if ptr1 > ptr2:
                    ptr1 += 1
                else:
                    ptr2 += 1
            
            elif heights[ptr1] > heights[ptr2]:
                ptr2 += 1
            else:
                ptr1 += 1
        
        return max_area