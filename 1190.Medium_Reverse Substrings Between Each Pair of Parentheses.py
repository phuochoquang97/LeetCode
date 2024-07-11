class Solution:
    def reverseParentheses(self, s: str) -> str:
        q = deque()
        paren_index = []

        for i in range(len(s)):
            if s[i] == "(":
                q.append(i)
            if s[i] == ")":
                j = q.pop()
                paren_index.append((j, i))

        sorted(paren_index).reverse()

        s_list = list(s)
        for l, r in paren_index:
            s_list[l:r] = reversed(s_list[l:r])

        return "".join(c for c in s_list if c not in "()")
