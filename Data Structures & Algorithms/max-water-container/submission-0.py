class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        curr_best=-float('inf')
        while left<right:
            height=min(heights[left], heights[right])
            width=abs(right-left)
            curr_best=max(curr_best, height*width)
            if height==heights[left]:
                left+=1
            else:
                right-=1
        return curr_best
        