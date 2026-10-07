class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        left=0
        right=1
        current_best=1
        s_hash={}
        s_hash[s[left]]=1
        while right<len(s):
            if s[right] not in s_hash:
                s_hash[s[right]]=1
                right+=1
            else:
                current_best=max(current_best, right-left)
                del s_hash[s[left]]
                left+=1
        return max(current_best, right-left)
            
            



