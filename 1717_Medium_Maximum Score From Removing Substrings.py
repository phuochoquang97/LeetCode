class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        min_val = min(x, y)
        max_val = max(x, y)

        m = {}
        if x > y:
            m[max_val] = "a"
            m[min_val] = "b"
        else:
            m[max_val] = "b"
            m[min_val] = "a"

        total_reward = 0
        stack = deque()
        for c in s:
            if c == m[min_val] and len(stack) > 0 and stack[-1] == m[max_val]:
                total_reward += max_val
                stack.pop()
            else:
                stack.append(c)
        s1 = list(stack)
        stack = deque()
        for c in s1:
            if c == m[max_val] and len(stack) > 0 and stack[-1] == m[min_val]:
                total_reward += min_val
                stack.pop()
            else:
                stack.append(c)

        return total_reward

# TLE
# class Solution:
#     def maximumGain(self, s: str, x: int, y: int) -> int:
#         total_reward = 0
#         max_point = max(x, y)
#         min_point = min(x, y)
#         m = {}
#         if x > y:
#             m[max_point] = "ab"
#             m[min_point] = "ba"
#         else:
#             m[max_point] = "ba"
#             m[min_point] = "ab"

#         position = s.find(m[max_point])
#         while position != -1:
#             s = s[:position] + s[position + 2:]
#             total_reward += max_point
#             position = s.find(m[max_point])

#         position = s.find(m[min_point])
#         while position != -1:
#             s = s[:position] + s[position + 2:]
#             total_reward += min_point
#             position = s.find(m[min_point])

#         return total_reward
