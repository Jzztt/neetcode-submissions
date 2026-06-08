class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            my_set = set()
            for j in range(9):
                is_valid = board[i][j]
                if is_valid in my_set:
                    return False
                elif is_valid != ".":
                    my_set.add(is_valid)
        
        for i in range(9):
            my_set = set()
            for j in range(9):
                is_valid = board[j][i]
                if is_valid in my_set:
                    return False
                elif is_valid != ".":
                    my_set.add(is_valid)
        
        start= [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)
        ]
        for init_row, init_colum in start:
            my_set = set()
            for i in range(init_row, init_row + 3):
                for j in range(init_colum, init_colum + 3):
                    value = board[i][j]
                    if value in my_set:
                         return False
                    elif value != ".":
                        my_set.add(value)
        return True







        