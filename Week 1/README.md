# SDLC — CS50 AI Week 1: Knights (Knights & Knaves)

## Planning:

The goal of this project was to build logical knowledge bases for each Knights and Knaves puzzle so that model_check could determine whether each character is a knight or a knave. The program would be successful if it correctly identified every character using only formal logic. All work had to be done in puzzle.py, while logic.py remained unchanged, and no extra libraries could be used. The key rules were that knights always tell the truth, knaves always lie, and each character must be exactly one of these.

## Analysis:

The project used logical tools from logic.py, including Symbols, And, Or, Not, Implication, and model_check. For each puzzle, spoken sentences were translated into propositional logic. If a character was a knight, their statement had to be true. If they were a knave, their statement had to be false. Each character also needed a constraint stating they could not be both a knight and a knave. In Puzzle 3, extra symbols were required to represent what A said, because B referred to A’s quoted words rather than only A’s identity.

## Design:

Each puzzle had its own knowledge base. Two symbols were created for each character, such as AKnight and AKnave. Every knowledge base included identity rules plus logical implications based on what each character said. For Puzzle 3, additional symbols were designed to track whether A said “I am a knight” or “I am a knave,” so B’s statement could be modeled correctly.

## Implementation:

All logic was written in puzzle.py. For each puzzle, identity constraints were added first, then translations of each character’s statements were encoded using Implication. In Puzzle 3, symbols for A’s spoken sentence were added before encoding B’s and C’s statements. The function model_check was then used to test which identities had to be true, and the results were printed.

## Testing and Troubleshooting:

Testing was done by running python puzzle.py and checking the output for each puzzle. When Puzzle 3 initially produced no results, this showed that the knowledge base was incomplete, which led to adding symbols for what A said. After updating the logic, all four puzzles produced correct and unique answers.

## Conclusion:

This project showed how propositional logic and model checking can be used to reason about truth and deception. By translating natural language statements into formal logic, the program was able to determine each character’s identity without manual reasoning.