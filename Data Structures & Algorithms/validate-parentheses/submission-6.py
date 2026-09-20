class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if len(stack)>0:
                    top=stack[-1]
                    if (i==')' and top!='(') or (i=='}' and top!='{') or (i==']' and top!='[') :
                        return False
                    else:
                        stack.pop()
                else:
                    return False

        return (len(stack)==0)

                
                



                