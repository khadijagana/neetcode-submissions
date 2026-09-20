class Solution:

    def encode(self, strs: List[str]) -> str:
        list_s=[]
        for i in range(len(strs)):
            length=len(strs[i])
            info=f"{length}#"
            info+=strs[i]
            list_s.append(info)
        s="".join(list_s)
        return s

    def decode(self, s: str) -> List[str]:
        OG=[]
        i=0
        while i < len(s):
            j=i
            while s[j].isdigit():
                current_word=""
                j+=1
            
            count=int(s[i:j])
            for a in range(j+1, j+1+count):
                current_word+=s[a]
            i=j+1+count
            OG.append(current_word)
                
            
        return OG
