from collections import defaultdict
from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod_store = defaultdict(int)

        # Fill the mod_store with remainders
        for a in arr:
            mod = a % k
            mod_store[mod] += 1

        # Check for the pairs
        for i in range(1, (k // 2) + 1):
            if mod_store[i] != mod_store[k - i]:
                return False

        # Special case for numbers divisible by k
        if mod_store[0] % 2 != 0:
            return False
        
        # Special case if k is even
        if k % 2 == 0 and mod_store[k // 2] % 2 != 0:
            return False

        return True
