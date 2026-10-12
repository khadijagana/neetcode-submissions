class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        max_len=0
        hash_m={}
        current_max=0
        while right<len(s):
            if s[right] not in hash_m:
                hash_m[s[right]]=1
                  
            else:
                hash_m[s[right]]+=1

            replacements_needed=(right-left+1)-max(hash_m.values())
            
            while replacements_needed>k:
                hash_m[s[left]]-=1
                left+=1
                replacements_needed=(right-left+1)-max(hash_m.values())


            current_max=max(current_max, right-left+1)
            right+=1


        return current_max