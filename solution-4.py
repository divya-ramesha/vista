matrix = [
    ["0", "0", "0", "0", "1", "0", "0"],
    ["0", "1", "1", "0", "1", "0", "0"],
    ["0", "1", "0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "0", "0", "0"],
    ["0", "1", "0", "1", "0", "1", "0"],
    ["0", "0", "1", "1", "0", "1", "0"],
    ["1", "0", "0", "0", "0", "1", "0"],
    ["0", "0", "1", "1", "1", "1", "0"]
]

def is_maze_traversible(matrix, start, goal, current_path):
    
    row, col = current_path[-1]
    if (row, col) == goal:
        return True
    for direction in [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]:
        new_row, new_col = direction
        if (0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] == "0" and (new_row, new_col) not in current_path):            
            current_path.append((new_row, new_col))
            if is_maze_traversible(matrix, start, goal, current_path):
                return True
            else:
                current_path.pop()

start = (0, 0)
goal = (len(matrix) - 1, len(matrix[0]) - 1)
result = [start]
if is_maze_traversible(matrix, start, goal, result):
    print("Success!")
else:
    print("Failure!")
