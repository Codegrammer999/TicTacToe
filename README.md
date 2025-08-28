# TicTacToe

A simple and fun command-line Tic-Tac-Toe game built with Python!

## Overview

This project is a classic implementation of the Tic-Tac-Toe game, inspired by a Python tutorial book. It's designed for two players and runs entirely in the terminal. The code is beginner-friendly and can be a great starting point for those learning Python or looking to build their own games.

**Now with a "You vs Computer" mode!**  
Challenge yourself by playing against the computer, or play with a friend in two-player mode.

## Features

- Two-player mode (X and O)
- Human vs Computer mode (play against a simple AI)
- **Unbeatable AI in Hard Mode using the Minimax algorithm**
- Simple, readable Python code
- Clear instructions and user prompts
- Input validation for moves
- Detects wins, draws, and invalid moves

## AI Difficulty

The computer opponent uses the **Minimax algorithm**, which explores all possible moves and chooses the one that maximizes its chance of winning (and minimizes the player's chance).  
👉 **This makes the AI unbeatable in Hard Mode.**

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Running the Game

1. Clone the repository:
    ```sh
    git clone https://github.com/Codegrammer999/TicTacToe.git
    ```
2. Navigate to the project directory where you cloned:
    ```sh
    e.g cd TicTacToe
    ```
3. Run the game:
    ```sh
    python game.py
    ```

> **Note:** The filename may be different if you renamed the main script file.

## How to Play

- The game is played on a 3x3 grid.
- Choose between two-player mode or play against the computer.
- Players take turns to input their moves (row and column).
- The first player to get three of their marks (X or O) in a row (horizontally, vertically, or diagonally) wins.
- If all 9 squares are filled and no player has three in a row, the game ends in a draw.

## Example Gameplay

```

  O | O |O
  -+-+-+-+-
    | X |O
  -+-+-+-+-
    |   |X
```

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request with improvements or new features.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

*Happy coding and enjoy playing Tic-Tac-Toe!*
