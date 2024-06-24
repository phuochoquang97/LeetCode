class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        projects = list(zip(difficulty, profit))
        projects.sort()  # sort projects based on the difficulty with ascending order

        worker.sort()
        max_profit = 0
        idx = 0
        current_max_profit = 0

        for w in worker:
            while (
                idx < len(projects) and projects[idx][0] <= w
            ):  # find project what has max profit and difficulty <= w
                current_max_profit = max(current_max_profit, projects[idx][1])
                idx += 1
            max_profit += current_max_profit

        return max_profit
