# SDLC for CS50 AI Week 0: Tic-Tac-Toe

## Planning
The goal of this project is to implement an AI that plays Tic-Tac-Toe optimally. The AI must choose the best move for the current player using the Minimax algorithm. The code must be written in `tictactoe.py`, and `runner.py` must remain unchanged. The project is complete when the game runs with `python runner.py` and the AI cannot be beaten with correct play.

## Analysis
The board is represented as a 3x3 list of lists containing `X`, `O`, or `EMPTY`. The program needs functions to determine whose turn it is, what moves are available, what happens after a move, whether there is a winner, whether the game is over, how to score terminal states, and how to select the optimal move. The Minimax algorithm evaluates future game states by exploring all valid actions until terminal states are reached, then propagates scores back up the recursion to choose the best move.

## Design
The solution is organized around required functions: `player`, `actions`, `result`, `winner`, `terminal`, `utility`, and `minimax`. `player` uses counts of X and O to decide the turn. `actions` scans the board and returns all empty cells. `result` returns a deep-copied board with the current player’s move applied and raises an exception for invalid actions. `winner` checks all rows, columns, and diagonals. `terminal` returns true if someone won or the board is full. `utility` assigns 1 for X win, -1 for O win, and 0 for a tie. `minimax` uses recursion to compute the optimal move by choosing the maximum score for X and the minimum score for O.

## Implementation
The required functions are implemented in `tictactoe.py` using only the standard library. A deep copy is created in `result` to avoid mutating the original board during search. `minimax` performs recursive evaluation of possible actions until a terminal state is reached, then returns the best action for the current player based on utility values.

## Testing and Troubleshooting
Testing is done by running `python runner.py` and verifying the AI always blocks wins and never loses. Additional tests include calling functions directly in the Python interpreter to confirm correct outputs for known boards, including winner detection for rows, columns, diagonals, and tie states. If behavior is incorrect, the main debugging focus is validating deep copies in `result`, ensuring `winner` checks all lines correctly, and confirming `minimax` alternates between maximizing for X and minimizing for O.

## Conclusion
This project implements a complete Tic-Tac-Toe AI by combining correct game-state evaluation with Minimax search. The result is an opponent that plays optimally and cannot be beaten with perfect play.