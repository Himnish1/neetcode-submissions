from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_visited = defaultdict(set)
        row_visited = defaultdict(set)
        square_visited = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in col_visited[j]:
                    return False
                if board[i][j] in row_visited[i]:
                    return False
                # calculate which square you're in
                mod_i = int(i // 3)
                mod_j = int(j // 3)
                square_number = mod_i*3+mod_j
                if board[i][j] in square_visited[square_number]:
                    return False

                # add to respective sets
                col_visited[j].add(board[i][j])
                row_visited[i].add(board[i][j])
                square_visited[square_number].add(board[i][j])
        return True
