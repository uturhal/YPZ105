# w14-11-tic-tac-toe.py — 3x3 tahta: gösterim ve kazanan kontrolü

EMPTY = " "

def show(board):
    print("   0   1   2")
    for i in range(3):
        print(f"{i}  " + " | ".join(board[i]))

def lines_of(board):
    """Kazanmaya aday 8 üçlü: 3 satır, 3 sütun, 2 köşegen."""
    triples = [row for row in board]
    triples += [[board[i][j] for i in range(3)] for j in range(3)]
    triples.append([board[i][i] for i in range(3)])
    triples.append([board[i][2 - i] for i in range(3)])
    return triples

def winner(board):
    """Kazanan işareti, kimse kazanmadıysa None döndürür."""
    for t in lines_of(board):
        if t[0] != EMPTY and t[0] == t[1] == t[2]:
            return t[0]
    return None

def is_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

game = [[EMPTY] * 3 for _ in range(3)]      # her satır AYRI bir liste
for i, j, mark in [(1, 1, "X"), (0, 0, "O"), (0, 1, "X"),
                   (2, 2, "O"), (2, 1, "X")]:
    game[i][j] = mark
show(game)
print("Aday üçlü:", len(lines_of(game)), " kazanan:", winner(game),
      " dolu mu?", is_full(game))

draw = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
show(draw)
print("Kazanan:", winner(draw), " dolu mu?", is_full(draw))
