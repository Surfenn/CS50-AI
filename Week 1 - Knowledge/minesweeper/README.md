# SDLC for CS50 AI Week 1: Minesweeper

## Planning
The goal of this project was to build an AI that can play Minesweeper intelligently using logical reasoning rather than guessing whenever possible. The program needed to use a knowledge-based agent that tracks safe moves and mines based on logical constraints. Success was defined as the AI correctly identifying safe cells and mines whenever logic made this possible. All work was completed in `minesweeper.py`, while `runner.py` remained unchanged, and no unauthorized libraries were used.

## Analysis
The board is represented as a grid where each cell may be a mine, safe, or unknown. The AI must maintain a knowledge base of logical sentences about which cells contain mines. Each time a safe cell is revealed, the number of neighboring mines provides new information that must be encoded as constraints. The agent must use this knowledge to mark known mines, identify safe moves, and avoid repeating actions. When logic alone is insufficient, the AI may choose a random move.

## Design
The solution was organized around the required methods in the `MinesweeperAI` class. The AI maintains a set of known safe cells, known mines, and a list of logical sentences representing constraints. Each sentence tracks a group of cells and how many of them are mines. When new information is received, the AI updates existing sentences and derives new ones until no further inferences can be made. Safe moves are chosen from known safe cells first, and random moves are selected only when necessary.

## Implementation
All logic was implemented in `minesweeper.py`. The `add_knowledge` method was responsible for creating new sentences based on revealed cells and updating the knowledge base. Helper methods such as `mark_mine` and `mark_safe` ensured consistency across all stored information. The `make_safe_move` function selected a move from known safe cells, while `make_random_move` selected from remaining unknown cells. The AI repeatedly refined its knowledge before making each move.

## Testing and Troubleshooting
Testing was done by running `python runner.py` and observing the AI’s behavior across multiple games. The AI was expected to avoid obvious mines, correctly flag known mines, and rarely guess. Debugging focused on verifying that sentences were updated properly, that safe cells were not mistakenly marked as mines, and that redundant moves were avoided. Edge cases such as fully revealed regions and zero-neighbor cells were also checked.

## Conclusion
This project demonstrated how logical reasoning can be used to solve uncertain problems like Minesweeper. By maintaining and u