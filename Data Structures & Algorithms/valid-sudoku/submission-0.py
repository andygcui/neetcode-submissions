class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen_row = set()
            seen_col = set()
            for j in range(9):
                if board[i][j] in seen_row and board[i][j] != ".":
                    return False
                else:
                    seen_row.add(board[i][j])
                if board[j][i] in seen_col and board[j][i] != ".":
                    return False
                else:
                    seen_col.add(board[j][i])
        
        for start_row in range(3):
            for start_col in range(3):
                seen_sub = set()

                for x in range(3):
                    for y in range(3):
                        value = board[3 * start_row + x][3 * start_col + y]
                        if value in seen_sub and value != ".":
                            return False
                        else:
                            seen_sub.add(value)
        return True


