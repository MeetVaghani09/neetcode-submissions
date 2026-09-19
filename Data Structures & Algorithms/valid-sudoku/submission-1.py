class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]    # digits seen in each row
        cols = [set() for _ in range(9)]    # digits seen in each column
        boxes = {}                          # digits seen in each 3x3 box

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":              # skip empty cells
                    continue

                box = (r // 3, c // 3)      # which 3x3 box this cell is in
                if box not in boxes:
                    boxes[box] = set()

                # duplicate found in row, column, or box
                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True


        