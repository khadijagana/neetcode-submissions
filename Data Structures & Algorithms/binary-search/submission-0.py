import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        cursor=math.ceil(len(nums)/2)-1
        left=0
        right=len(nums)-1
        while (nums[cursor] != target and left<right):
            if nums[cursor]<target:
                left=cursor+1
                cursor=cursor+math.ceil((right-cursor)/2)
            else:
                right=cursor-1
                cursor=cursor-math.ceil((cursor-left)/2)
        if nums[cursor]==target:
            return cursor
        
        return -1
