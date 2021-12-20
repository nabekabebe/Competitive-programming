class Solution:
    def isValid(self, s: str) -> bool:
        op = ['(', '{', '[']
        ed = [')','}',']']
        
        stack = []
        for i in s:
            if i in op:
                stack.append(i)
            else:
                if len(stack) > 0:
                    last = stack.pop()
                    if op.index(last) != ed.index(i):
                        return False
                else:
                    return False
                
        return True if len(stack) == 0 else False
