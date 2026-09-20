class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(nums))!=0:
            unique_nums=[]
            for i in range(len(nums)):
                if nums[i] in (unique_nums):
                    return True
                unique_nums.append(nums[i])
        return False
