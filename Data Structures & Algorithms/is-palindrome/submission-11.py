class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=s.replace(" ","")
        left=0
        right=len(new_s)-1
        while left < right :
            if not new_s[left].isalnum():
                left+=1
            elif not new_s[right].isalnum():
                right-=1
            elif new_s[left].lower()==new_s[right].lower():
                left+=1
                right-=1
            else:
                return False
        return True