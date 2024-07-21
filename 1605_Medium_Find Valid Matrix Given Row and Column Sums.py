class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n_row = len(rowSum)
        n_col = len(colSum)

        ret = [[0] * n_col for _ in range(n_row)]

        # assign the first value of each row with rowSum
        for i in range(n_row):
            ret[i][0] = rowSum[i]

        # now process each col
        for j in range(n_col):
            # get the current sum of the col
            current_col_sum = 0
            for i in range(n_row):
                current_col_sum += ret[i][j]

            current_row = 0
            while current_col_sum > colSum[j]:
                # get the difference between current_col_sum and valid col_sum
                diff = current_col_sum - colSum[j]

                # calculate the amount that can be subtracted
                max_shift = min(diff, ret[current_row][j])
                ret[current_row][j] -= max_shift

                # assign next value of the row to validate the sum of current row
                ret[current_row][j + 1] = max_shift

                # reduce current_col_sum
                current_col_sum -= max_shift

                # move to the next row
                current_row += 1

        return ret
