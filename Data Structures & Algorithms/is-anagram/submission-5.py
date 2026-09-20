class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        hash_map1={}
        hash_map2={}

        for i in range (len(s)):
            if s[i] in hash_map1:
                hash_map1[s[i]]+=1
            else:
                hash_map1[s[i]]=1
        
        for j in range(len(t)):
            if t[j] in hash_map2:
                hash_map2[t[j]]+=1
            else:
                hash_map2[t[j]]=1

        return hash_map1==hash_map2
            
