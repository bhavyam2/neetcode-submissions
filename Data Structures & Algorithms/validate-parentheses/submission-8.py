class Solution:
    def isValid(self, s: str) -> bool:
        paren = {')': '(', ']': '[', '}':'{'}
        stack = []
        for i in s:
            if i in paren:
                if (len(stack) > 0) and paren[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack