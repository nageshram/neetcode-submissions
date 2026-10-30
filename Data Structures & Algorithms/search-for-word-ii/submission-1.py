class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = {}

        # Build Trie
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["$"] = word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, parent):

            ch = board[r][c]

            if ch not in parent:
                return

            node = parent[ch]

            # Word found
            if "$" in node:
                res.append(node.pop("$"))

            # Mark visited
            board[r][c] = "#"

            # Explore four directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] != "#"):

                    dfs(nr, nc, node)

            # Backtrack
            board[r][c] = ch

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:
                    dfs(i, j, trie)

        return res