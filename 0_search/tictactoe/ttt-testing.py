import tictactoe as ttt

initial_board = ttt.initial_state()

# should print X
# print(f'{ttt.player(initial_board)}')
# 
# print(f'{ttt.actions(initial_board)}')
# 
print(f'{ttt.winner(ttt.result(initial_board, (1, 1)))}')

# print(ttt.minimax(initial_board))

winning_lines = []
grid_range = range(0, 3)

for row_idx in grid_range:
        winning_lines.append([ (row_idx, column_idx) for column_idx in grid_range ])
        winning_lines.append([ (column_idx, row_idx) for column_idx in grid_range ])

winning_lines.append([ (idx, idx) for idx in grid_range ])
winning_lines.append([ (len(grid_range) - idx - 1, idx) for idx in grid_range ])

print(winning_lines)
print(len(winning_lines))