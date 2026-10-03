class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col, index):
            if (
                row < 0 or row >= len(board)
                or col < 0 or col >= len(board[0])
                or (row, col) in visited
                or board[row][col] != word[index]
            ):
                return False

            if index == len(word) - 1:
                return True

            visited.add((row, col))

            for dr, dc in direction:
                nr, nc = row + dr, col + dc

                if dfs(nr, nc, index + 1):
                    return True

            visited.remove((row, col))
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True

        return False