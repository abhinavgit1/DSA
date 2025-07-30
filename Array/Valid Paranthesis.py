class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        end = {')':'(','}':'{',']':'['}
        for el in s:
            if el not in end:
                stack.append(el)
            else:
                if stack and stack[-1]==end[el]:
                    stack.pop()
                else:
                    return False
        return not stack