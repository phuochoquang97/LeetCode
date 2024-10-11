class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # add index for each arrival
        for i in range(len(times)):
            times[i] = (times[i][0], times[i][1], i)

        # sort by arrival time
        times = sorted(times)

        # min-heap to track available chairs
        available_chairs = list(range(len(times)))
        heapq.heapify(available_chairs)

        # min-heap to track when chairs will be free by leave times
        occupied_chairs = []

        for current_arrival in range(len(times)):
            arrival_time = times[current_arrival][0]
            leave_time = times[current_arrival][1]
            friend_idx = times[current_arrival][2]

            # release chairs of friend who already left
            while occupied_chairs and occupied_chairs[0][0] <= arrival_time:
                leave, chair_idx = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, chair_idx)

            chair_idx = heapq.heappop(available_chairs)

            if friend_idx == targetFriend:
                return chair_idx

            # push the current friend's leave time and chair to occupied chairs
            heapq.heappush(occupied_chairs, (leave_time, chair_idx))

        return -1
