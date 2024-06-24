class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        r = position[-1] - position[0]  # max distance
        l = 1  # min distance

        def canPlace(distance):
            count = 1
            last_position = position[0]
            for i in range(1, len(position)):
                if position[i] - position[last_position] >= distance:
                    last_position = position[i]
                    count += 1

                    if count == m:
                        return True

            return False

        while l < r:
            mid = l + (r - l) // 2
            if canPlace(mid):
                l = mid
            else:
                r = mid - 1

        return l
