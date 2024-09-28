class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # max_ship = sum(weights) -> O(logN) binary search
        # how to check if current_ship is possible? -> O(N)
        def is_possible(current_ship):
            count_day = 0
            current_weight = 0
            for w in weights:
                if w > current_ship:
                    return False
                current_weight += w
                if current_weight > current_ship:
                    current_weight = w
                    # take 1 day
                    count_day += 1
                    if count_day > days:
                        return False

            # the last current_weight will take an extra day
            return count_day <= days - 1

        min_ship = 1
        max_ship = sum(weights)
        while min_ship < max_ship:
            mid = min_ship + (max_ship - min_ship) // 2
            if is_possible(mid):
                max_ship = mid
            else:
                min_ship = mid + 1
            # print(f"min: {min_ship}, max: {max_ship}")

        return min_ship
