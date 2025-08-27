class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c:i for i,c in enumerate(s)}
        stack, seen = [], set()
        for i, c in enumerate(s):
            if c in seen: 
                continue
            while stack and c < stack[-1] and last[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(c); seen.add(c)
        return ''.join(stack)
        