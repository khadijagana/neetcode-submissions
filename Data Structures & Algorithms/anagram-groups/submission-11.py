class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        ordered_strs=strs.copy()
        for i in range (len(strs)):
            ordered_strs[i]=sorted(strs[i])
        for j in range (len(ordered_strs)):
            key = ''.join(ordered_strs[j])
            if key not in seen:
                seen[key]=[strs[j]]
            else:
                seen[key].append(strs[j])
        return list(seen.values() )