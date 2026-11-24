class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Brute Force Approach

        #rows
        for row in board:
            seen = set()
            for square in row:
                if square in seen and square != ".":
                    print(f"row : {row}")
                    return False
                else:
                    seen.add(square)
        

        #cols
        for i in range(9):
            seen = set()
            for j in range(9):
                square = board[j][i]
                if square in seen and square != ".":
                    print("col")
                    return False
                else:
                    seen.add(square)
        
        #box

        for i in range(9):
            seen = set()
            for j in range(9):
                square = board[j % 3 + (i % 3) * 3][ j // 3 + (i // 3) * 3]
                if square in seen and square != ".":
                    print("box")
                    return False
                else:
                    seen.add(square)
        

        return True
                