class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brace_map = {']': '[', '}': '{', ')': '('}
        
        for b in s:
            if b in brace_map:
                if stack and stack[-1] == brace_map[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False
