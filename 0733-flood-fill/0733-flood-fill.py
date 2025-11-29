from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image 

        rows, cols = len(image), len(image[0])
        stack = [(sr, sc)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while stack:
            r, c = stack.pop()

            if image[r][c] == original:
                image[r][c] = color

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if image[nr][nc] == original:
                            stack.append((nr, nc))

        return image
     