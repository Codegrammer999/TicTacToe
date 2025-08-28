import random

# Console Colors
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Game Board
theBoard = {
    "top-L": " ", "top-M": " ", "top-R": " ",
    "mid-L": " ", "mid-M": " ", "mid-R": " ",
    "low-L": " ", "low-M": " ", "low-R": " "
}

# Display Board
def printBoard(board):
    print(f"\n" + 
        board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
    print(f" -+-+-+- ")
    print(board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
    print(f" -+-+-+- ")
    print(board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'] + "\n")

# Valid Moves List
def availableMoves(board):
    return [k for k, v in board.items() if v == " "]

# Check if no moves left
def isNoMoreMoves(board):
    return all(v != " " for v in board.values())

# Check Wins
def checkWinner(board):
    wins = [
        ["top-L", "top-M", "top-R"],
        ["mid-L", "mid-M", "mid-R"],
        ["low-L", "low-M", "low-R"],
        ["top-L", "mid-L", "low-L"],
        ["top-M", "mid-M", "low-M"],
        ["top-R", "mid-R", "low-R"],
        ["top-L", "mid-M", "low-R"],
        ["top-R", "mid-M", "low-L"]
    ]
    for line in wins:
        if board[line[0]] == board[line[1]] == board[line[2]] != " ":
            return board[line[0]]  # "X" or "O"
    return None

# Minimax AI
def minimax(board, isMaximizing):
    winner = checkWinner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if isNoMoreMoves(board): return 0

    if isMaximizing:  # Computer O
        bestScore = -999
        for move in availableMoves(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "
            bestScore = max(bestScore, score)
        return bestScore
    else:  # Player X
        bestScore = 999
        for move in availableMoves(board):
            board[move] = "X"
            score = minimax(board, True)
            board[move] = " "
            bestScore = min(bestScore, score)
        return bestScore

def getBestMove(board):
    bestScore = -999
    bestMove = None
    for move in availableMoves(board):
        board[move] = "O"
        score = minimax(board, False)
        board[move] = " "
        if score > bestScore:
            bestScore = score
            bestMove = move
    return bestMove

# Game Loop
def gamePlay(vsAI=False, difficulty="easy"):
    turn = "X"
    while True:
        printBoard(theBoard)

        winner = checkWinner(theBoard)
        if winner:
            print(f"{GREEN}{winner} wins! 🎉{RESET}")
            break
        if isNoMoreMoves(theBoard):
            print(f"{YELLOW}It's a Draw! 🤝{RESET}")
            break

        if vsAI and turn == "O":  # Computer move
            if difficulty == "easy":
                move = random.choice(availableMoves(theBoard))
            else:
                move = getBestMove(theBoard)
            print(f"{CYAN}Computer chooses {move}{RESET}")
        else:  # Player move
            move = input(f"\n{turn}'s turn. Choose a move {availableMoves(theBoard)}: ").strip()
            if move not in availableMoves(theBoard):
                print(f"{RED}Invalid move! Try again.{RESET}")
                continue

        theBoard[move] = turn
        turn = "O" if turn == "X" else "X"

# Main Menu
def main():
    print(f"{CYAN}🎮 Welcome to Tic-Tac-Toe!{RESET}\n")

    mode = ""
    while mode not in ["1", "2"]:
        print("Choose a mode:")
        print("1: You vs Computer")
        print("2: 2 Players")
        mode = input("\nEnter option (1 or 2): ").strip()
        if mode not in ["1", "2"]:
            print(f"{RED}Invalid option, please enter 1 or 2.{RESET}\n")

    if mode == "1":
        diff = ""
        while diff not in ["1", "2"]:
            print("\nSelect Difficulty:")
            print("1: Easy")
            print("2: Hard")
            diff = input("\nEnter option (1 or 2): ").strip()
            if diff not in ["1", "2"]:
                print(f"{RED}Invalid option, please enter 1 or 2.{RESET}\n")

        difficulty = "easy" if diff == "1" else "hard"
        gamePlay(vsAI=True, difficulty=difficulty)
    else:
        gamePlay(vsAI=False)

    again = ""
    while again not in ["1", "2"]:
        again = input("\nPlay again?\n1: Yes\n2: No (Exit)\n\nEnter option: ").strip()
        if again not in ["1", "2"]:
            print(f"{RED}Invalid option, please enter 1 or 2.{RESET}\n")

    if again == "1":
        global theBoard
        theBoard = {key: " " for key in theBoard}  # reset board
        main()
    else:
        print(f"{CYAN}Thanks for playing! Bye 👋{RESET}")
        print(f"{GREEN}Please support by leaving a star and follow on github.")
# Start
if __name__ == "__main__":
    main()
