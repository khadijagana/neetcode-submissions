class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map={}
        for i in range (len(strs)):
            curr=[0]*26
            for j in strs[i]:
                index=ord('a')-ord(j)
                curr[index]+=1
            key=tuple(curr)
            if key not in hash_map:
                hash_map[key]=[strs[i]]
            else:
                hash_map[key].append(strs[i])
        return list(hash_map.values())