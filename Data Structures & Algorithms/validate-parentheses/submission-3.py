class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        if len(s)%2 ==1:
            return False
        for i in range(len(s)):
            if s[i] == '(':
                l.append(1)
            elif s[i] == '[':
                l.append(2)
            elif s[i] =='{':
                l.append(3)
            else:
                if len(l)>0:
                    value = l.pop()
                else:
                    value = 0
                if s[i] == ')':
                    c = -1
                elif s[i] == ']':
                    c = -2
                elif s[i] =='}':
                    c = -3
                else:
                    c = -4
                if c+value != 0:
                    return False
        if len(l)>0:
            return False
        return(True)        

        