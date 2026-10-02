class Solution:
    def isValid(self, s: str) -> bool:
        closing = [')', ']', '}']
        my_set = set(closing)

        stack = []
        for c in s:
            if c in my_set:
                if not stack:
                    return False
                else:
                    top = stack[-1]
                    stack.pop()

                    if (c == ')' and top != '(') or (c == ']' and top != '[') or (c == '}' and top != '{'):
                        return False

            else:
                stack.append(c)

        return len(stack) == 0





