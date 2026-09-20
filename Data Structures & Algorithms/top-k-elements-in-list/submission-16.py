class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        ordered_freq={}
        n=len(nums)
        result=[]
        tmp=0
        for i in range(n):
            if nums[i] not in hash_map:
                hash_map[nums[i]]=1
            else:
                hash_map[nums[i]]+=1
        
        for key, val in hash_map.items():
            if val not in ordered_freq:
                ordered_freq[val]=[key]
            else:
                ordered_freq[val].append(key)   
        
        for j in range(n,-1,-1):
            if j in ordered_freq:
                for element in ordered_freq[j]:
                    result.append(element)
                    tmp+=1
                    if tmp==k:
                        return result

        return []
        
        