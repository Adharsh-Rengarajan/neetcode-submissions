class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                digit = board[i][j]

                value = int(digit) - 1
                value = 1 << value

                if(value & rows[i]):
                    return False
                if (value & cols[j]):
                    return False
                if (value & squares[(i // 3) * 3 + (j // 3)]):
                    return False

                rows[i] |= (value)
                cols[j] |= (value)
                squares[(i // 3) * 3 + (j // 3)] |= (value)

        return True
