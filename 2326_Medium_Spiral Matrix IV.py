# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ret = [[-1] * n for _ in range(m)]
        current_row, current_col = 0, 0

        current = head
        direction = "e"
        max_row, min_row = m - 1, 0
        max_col, min_col = n - 1, 0
        while current:
            # todo: fill in the matrix
            ret[current_row][current_col] = current.val

            if direction == "e":
                if current_col == max_col:
                    direction = "s"
                    min_row += 1
                    current_row = min_row
                    current_col = max_col
                else:
                    current_col += 1

            elif direction == "s":
                if current_row == max_row:
                    direction = "w"
                    max_col -= 1
                    current_row = max_row
                    current_col = max_col
                else:
                    current_row += 1

            elif direction == "w":
                if current_col == min_col:
                    direction = "n"
                    max_row -= 1
                    current_row = max_row
                    current_col = min_col
                else:
                    current_col -= 1

            elif direction == "n":
                if current_row == min_row:
                    direction = "e"
                    min_col += 1
                    current_row = min_row
                    current_col = min_col
                else:
                    current_row -= 1

            current = current.next

        return ret
