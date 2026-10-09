class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]: return 0
        nums.sort()
        numb=1
        current_max=numb
        for i in range (len(nums)-1):
            if nums[i+1]==nums[i]+1:
                numb+=1                
            elif nums[i+1]!=nums[i]:
                current_max=max(current_max, numb)
                numb=1
        
        return max(current_max, numb)