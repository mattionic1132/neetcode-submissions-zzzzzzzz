class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in closeToOpen:
                #make sure stack not empty and make sure top element is matching
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
            
                #empty or not matching
                else: 
                    return False
            
            else: 
                stack.append(char)

        if not stack: 
            return True 
        else: 
            return False