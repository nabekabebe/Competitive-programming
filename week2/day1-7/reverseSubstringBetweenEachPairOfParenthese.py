class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for i in s:
            if i == ')':
                result  = []
                last = stack.pop()
                while last != '(':
                    result.append(last)
                    last = stack.pop()
                for i in result:
                    stack.append(i) 
                
            else:
                stack.append(i)
        
        final = ""
        for i in stack:
            final += i
            
        return final
