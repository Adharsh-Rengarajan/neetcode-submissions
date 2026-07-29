class Solution:
    def isValid(self, s: str) -> bool:
        verification_map = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []

        for i in s:
            if i in verification_map:
                if stack!=[] and stack[-1] == verification_map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)


        return stack == []