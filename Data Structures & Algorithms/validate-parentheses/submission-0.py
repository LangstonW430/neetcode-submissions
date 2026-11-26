class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            if not stack:
                stack.append(item)
            elif (stack[-1] == "(" and item == ")") or (stack[-1] == "{" and item == "}") or (stack[-1] == "[" and item == "]"):
                stack.pop()
            else:
                stack.append(item)
        

        return not stack
