# kakao_2016int_01.py

def solution(board, moves):
    answer = 0
    set_board = board
    out_board = []

    for i in moves:
        for j, val in enumerate(set_board):
            if (val[i - 1] != 0):
                out_board.append(val[i - 1])
                if (len(out_board) >= 2 and out_board[-1] == out_board[-2]):
                    out_board.pop()
                    out_board.pop()
                    answer += 2
                set_board[j][i - 1] = 0
                break

    return answer