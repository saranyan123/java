class Solution:
    def findWords(self, board, words):
        res = []
        trie = {}
        
        # Build Trie
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = word
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, parent):
            char = board[r][c]
            curr_node = parent[char]
            
            # Check if we found a word
            word_found = curr_node.pop('#', None)
            if word_found:
                res.append(word_found)
            
            # Mark as visited
            board[r][c] = '@'
            
            # Explore neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node:
                    dfs(nr, nc, curr_node)
            
            # Restore board (backtrack)
            board[r][c] = char
            
            # Optimization: remove the leaf node
            if not curr_node:
                parent.pop(char)

        # Start search from every cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r, c, trie)
        
        return res
