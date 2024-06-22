class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        if  s[0] not in ["(","{","["]:
            return False
        for i in s:
            
            if i == "(":
                stack.insert(0, ")")
            elif i == "{":
                stack.insert(0, "}")
            elif i == "[":
                stack.insert(0, "]")
            elif i == ")":
                if len(stack) == 0:
                    return False
                if stack.pop(0) != ")":
                    return False
            elif i == "}":
                if len(stack) == 0:
                    return False
                if stack.pop(0) != "}":
                    return False
            elif i == "]":
                if len(stack) == 0:
                    return False
                if stack.pop(0) != "]":
                    return False
        if stack == []:
            return True
        else:
            return False