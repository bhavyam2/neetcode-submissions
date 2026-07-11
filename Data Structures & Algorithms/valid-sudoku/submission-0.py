class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        for i in range (0,9):
            for x in range(0,9):
                if board[i][x] == ".":
                    continue
                if board[i][x] in rows[i] or (board[i][x] in columns[x]) or (board[i][x] in squares[(i // 3, x // 3)]):
                    return False
                
                rows[i].add(board[i][x])
                columns[x].add(board[i][x])
                squares[(i//3, x//3)].add(board[i][x])
            
        print(squares)
        return True