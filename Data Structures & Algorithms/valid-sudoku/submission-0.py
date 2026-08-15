class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_box_len = 3
        box_len = 9 
        seen_sub_box = [[set() for _ in range(sub_box_len)] for _ in range(sub_box_len)]
        #seen_sub_box = defaultdict(set)

        for row in board:
            seen_row = set()
            for item in row:
                if item ==".":
                    continue
                if item in seen_row:
                    return False

                seen_row.add(item)
        for i in range(box_len):
            seen_col = set()
            for j in range(box_len):
                if board[j][i] ==".":
                    continue
                if board[j][i] in seen_col:
                    return False
                
                seen_col.add(board[j][i])
        for i in range(box_len):
            for j in range(box_len):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen_sub_box[i//sub_box_len][j//sub_box_len]:
                    return False
                else:
                    seen_sub_box[i//sub_box_len][j//sub_box_len].add(board[i][j])
        return True

            


