class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        op = set(["*", "/","+", "-"])
        stack = []
        
        for i in tokens:
            if i in op: 
                num1 = stack.pop()
                num2 = stack.pop()
                if i == '*':
                    result = int(num2) * int(num1)
                elif i == '/':
                    res = int(num2) * int(num1)
                    result = abs(int(num2)) //  abs(int(num1))
                    if res < 0:
                        result *= -1
                elif i == '+':
                    result = int(num2) + int(num1)
                elif i == '-':
                    result = int(num2) - int(num1)
                stack.append(str(result))
            else:
                stack.append(i)
        
        return int(stack[0])
