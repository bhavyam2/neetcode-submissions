from collections import deque

class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        start = image[sr][sc]
        ROWS, COLS = len(image), len(image[0])

        def neighbors(row, col):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (0 <= nr < ROWS and 0 <= nc < COLS
                        and image[nr][nc] == start):
                    yield nr, nc

        queue = deque([(sr, sc)])
        visited = {(sr, sc)}

        while queue:
            row, col = queue.popleft()
            image[row][col] = color

            for nr, nc in neighbors(row, col):
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return image