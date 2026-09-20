class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        pre=[1]*len(nums)
        suff=[1]*len(nums)
        result=[]
        for i in range(len(nums)):
            if i>0:
                new_pre=pre[i-1]*nums[i-1]
                pre[i]=new_pre
        for j in range(len(nums)-1, -1, -1):
            if j<len(nums)-1:
                new_suff=suff[j+1]*nums[j+1]
                suff[j]=new_suff
        for j in range(len(pre)):
            result.append(pre[j]*suff[j])
        return result

             