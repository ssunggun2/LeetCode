# class Solution:
#     def reverseParentheses(self, s: str) -> str:
#         stack = []
        
#         for char in s:
#             if char == ')':
#                 # Pop characters until finding the opening parenthesis '('
#                 temp = []
#                 while stack and stack[-1] != '(':
#                     temp.append(stack.pop())
#                 # Pop the opening parenthesis '('
#                 if stack:
#                     stack.pop()
#                 # Reverse the substring and push it back to stack
#                 stack.extend(temp)
#             else:
#                 # Push current character to stack
#                 stack.append(char)
        
#         # Join all characters to form the final result
#         return ''.join(stack)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for i in s:
            if i == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                if stack:
                    stack.pop()
                stack.extend(temp)
            else:
                stack.append(i)
        return ''.join(stack)