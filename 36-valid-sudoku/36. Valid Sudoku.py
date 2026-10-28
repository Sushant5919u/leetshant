
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

     
        def has_duplicate(items):
            seen = set()

            for num in items:
                if num == ".":
                    continue

                if num in seen:
                    return True

                seen.add(num)

            return False

     
        for row in board:
            if has_duplicate(row):
                return False

      
        for col in range(9):
            column = []

            for row in range(9):
                column.append(board[row][col])

            if has_duplicate(column):
                return False

        
        for start_row in (0, 3, 6):
            for start_col in (0, 3, 6):
                box = []

                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        box.append(board[r][c])

                if has_duplicate(box):
                    return False

        
        return True
