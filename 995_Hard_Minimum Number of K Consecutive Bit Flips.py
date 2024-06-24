class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        ret = 0
        q = deque()  # store index that is flipped

        for i in range(len(nums)):
            while q and i - k + 1 > q[0]:
                q.popleft()

            if (nums[i] + len(q)) % 2 == 0:  # flip
                if i + k > len(nums):
                    return -1

                ret += 1
                q.append(i)

        return ret


