class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_nums={}
        for i in range(len(nums)):
            if nums[i] in hash_nums:
                return True
            else:
                hash_nums[nums[i]]= 1
        return False
