class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        my_map = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != my_map[i]:
                    return False
        return len(stack) == 0


        