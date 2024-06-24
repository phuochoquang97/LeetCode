class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:  # impossible case
            return -1

        l = min(bloomDay)
        r = max(bloomDay)

        def canMakeBouquets(day: int) -> bool:
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloomDay <= day:
                    flowers += 1
                    if flowers == k:  # can make a bouquet
                        bouquets += 1
                        flowers = 0  # reset count number of flowers
                else:
                    flowers = 0

                if bouquets >= m:
                    return True

            return bouquets >= m

        while l < r:
            mid = l + (r - l) // 2
            if canMakeBouquets(mid):
                r = mid
            else:
                l = mid + 1

        return r
