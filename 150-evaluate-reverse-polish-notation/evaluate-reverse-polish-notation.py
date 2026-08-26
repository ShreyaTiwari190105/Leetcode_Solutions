class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                
                first = stack.pop()
                second = stack.pop()

                if token == "+":
                    result = second + first
                
                if token == "-":
                    result = second - first

                if token == "*":
                    result = second * first

                if token == "/":
                    result = int(second / first)

                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]