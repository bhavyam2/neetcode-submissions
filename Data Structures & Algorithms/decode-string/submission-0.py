class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0
        for i in s:
            if i.isdigit():
                curr_num = curr_num * 10 + int(i)
            
            elif i == "[":
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0

            elif i == "]":
                prev_str, num = stack.pop()
                curr_str = prev_str + (curr_str * num)
            
            else:
                curr_str += i

        return curr_str