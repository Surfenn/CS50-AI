# SDLC — CS50 AI Week 1: Knights (Knights & Knaves)

## Planning:

The goal of this project was to create a logical knowledge base for each Knights and Knaves puzzle so the program could determine whether each character is a knight or a knave. Success was defined as the program correctly identifying every character using logical reasoning rather than hardcoded answers. All logic had to be written in logic.py, and no other files could be modified or additional libraries imported. The core assumptions of the puzzle were that knights always tell the truth, knaves always lie, and each character must be exactly one of these.

## Analysis:

The project used logical tools from logic.py, including Symbols, And, Or, Not, Implication, Biconditional, and model_check. For each puzzle, English statements had to be translated into formal logic. If a character was a knight, their statement had to be true. If they were a knave, their statement had to be false. Every character also required a constraint stating they could not be both a knight and a knave at the same time.

## Design:

Each puzzle was built with its own knowledge base. Two symbols were created for each character, such as AKnight and AKnave. The knowledge base always included identity rules and logical implications based on what each character said. More complex statements were split into smaller logical pieces before being combined with And or Or. This kept the structure consistent across all puzzles.

## Implementation:

All implementation occurred inside logic.py. Identity rules were added first, followed by logical translations of each character’s statements. These statements were then connected to the speaker using implications. Finally, model_check was used to determine whether each character must be a knight or a knave, and the results were printed.

## Testing and Troubleshooting:

Testing involved running the program for each puzzle and checking that the results were logically correct and free of contradictions. When errors occurred, constraints were added one at a time to identify the issue. Common problems included missing identity rules or incorrectly written logical expressions, which were fixed through careful revision.

## Conclusion:

This project demonstrated how formal logic can be used to reason about truth and deception. It showed how knowledge bases and model checking allow an AI system to draw conclusions from structured information, strengthening both logical reasoning and problem solving skills.