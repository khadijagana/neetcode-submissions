class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        copy_nums=sorted(nums)
        for i in range(0,len(copy_nums)-2):
            left=i+1
            right=len(copy_nums)-1
            while left<right:
                curr=copy_nums[left]+copy_nums[right]
                if -(copy_nums[i])<curr:
                    right-=1
                elif -(copy_nums[i])>curr:
                    left+=1
                else:
                    if (i!=left and i!=right and left!=right and [copy_nums[left],copy_nums[i],copy_nums[right]] not in result):
                        result.append([copy_nums[left],copy_nums[i],copy_nums[right]])
                    left+=1
                    right-=1
                        
        return result
            