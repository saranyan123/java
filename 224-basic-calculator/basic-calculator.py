class Solution:
    def calculate(self, s):
        stack = []
        current_num = 0
        result = 0
        sign = 1  # 1 represents +, -1 represents -

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '+':
                result += sign * current_num
                current_num = 0
                sign = 1
            elif char == '-':
                result += sign * current_num
                current_num = 0
                sign = -1
            elif char == '(':
                # Save the result and sign to the stack
                stack.append(result)
                stack.append(sign)
                # Reset for the parenthesis content
                result = 0
                sign = 1
            elif char == ')':
                result += sign * current_num
                current_num = 0
                # Apply sign from before the '('
                result *= stack.pop()
                # Add the result from before the '('
                result += stack.pop()
        
        return result + (sign * current_num)

