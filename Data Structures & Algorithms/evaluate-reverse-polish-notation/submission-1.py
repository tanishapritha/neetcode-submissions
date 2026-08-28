class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))

            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if t == "+":
                    num = num1 + num2
                elif t == "-":
                    num = num1 - num2
                elif t == "*":
                    num = num1 * num2
                else:
                    num = int(num1 / num2)
                
                stack.append(num)

        return stack.pop()

