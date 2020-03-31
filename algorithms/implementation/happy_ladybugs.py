def happyLadybugs(b):
    empty   = "_"
    board   = list(b)

    for i in b:
        if b.count(i) <= 1 and i != "_":
            return "NO"
    
    if all(i == "_" for i in b ):
        return "YES"

    

    i = 1
    while(i < len(board) - 1):
        if i == 0 and board[i] != empty and board[i+1] != board[i]:
            if board[i+1] == empty:
                for j in range(len(board)):
                    if board[j] == board[i] and i != j:
                        board[i+1] = board[j]
                        board[j] = empty
        elif i > 0 and i < len(board):
            if board[i] != board[i-1] and board[i] != board[i+1]:
                if board[i-1] == empty:
                    for j in range(len(board)):
                        if board[j] == board[i] and i != j:
                            board[i-1] = board[j]
                            board[j] = empty
                elif board[i+1] == empty:
                    for j in range(len(board)):
                        if board[j] == board[i] and i != j:
                            board[i+1] = board[j]
                            board[j] = empty
        elif i == len(board) and board[i] != empty and board[i-1] != board[i]:
            if board[i-1] == empty:
                for j in range(len(board)):
                    if board[j] == board[i] and i != j:
                        board[i-1] = board[j]
                        board[j] = empty
        i += 1
    return "YES"

print(happyLadybugs("_"))
print(happyLadybugs("RBRB"))
print(happyLadybugs("RRRR"))
print(happyLadybugs("BBB"))
print(happyLadybugs("BBB_"))






                

