# SDLC For Crossword Generator

## Planning

### Goal:
Implement the required functions so the program can generate a valid crossword puzzle using a constraint satisfaction approach.

The following 8 functions are required:

**Enforce Node Consistency**  
Update each variable’s domain so that only words with the correct length remain.

**Revise**  
Ensure arc consistency between two variables. If a word in the first variable’s domain cannot match any word in the second variable’s domain at the overlap position, remove it.

**AC3**  
Apply arc consistency across variables until no more changes occur or a domain becomes empty.

**Assignment Complete**  
Check whether all crossword variables have been assigned a word.

**Consistent**  
Check whether an assignment satisfies all constraints. Words must be the correct length, must not repeat, and overlapping letters must match.

**Order Domain Values**  
Return the domain values for a variable ordered by the number of values they eliminate from neighboring variables.

**Select Unassigned Variable**  
Choose the next unassigned variable. Select the variable with the fewest remaining domain values. If there is a tie, choose the variable with the most neighbors.

**Backtrack**  
Use recursive search to assign words to variables until a complete solution is found or all options are exhausted.

### Success Criteria:
The program takes a crossword structure and a word list as input and returns a valid filled crossword that satisfies all constraints.

### Project Requirements:
- `crossword.py` must not be modified.
- Only the specified functions in `generate.py` should be implemented.
- Additional helper functions may be created if needed.
- Only Python standard library modules may be used.

---

# Analysis

### Tools:
- Python
- Provided crossword framework
- Constraint Satisfaction Problem methods

### Assets Provided:
- `crossword.py`
- Partial implementation of `generate.py`
- Crossword structure files
- Word list files

### Data Provided:
Structure files define which cells contain letters.

Word files contain the list of words that may be used in the puzzle.

### Problem Breakdown:
The crossword puzzle can be modeled as a constraint satisfaction problem.

- Each crossword slot is a **variable**
- Each variable has a **domain of possible words**
- Word length is a **unary constraint**
- Overlapping letters create **binary constraints**
- Words must be unique

The algorithm reduces domains using constraint propagation and then uses recursive search to assign words.

---

# Timeline & Steps

### Implement `enforce_node_consistency`
Remove words from a variable’s domain if their length does not match the slot length.

### Implement `revise`
Compare two variables that overlap.

If a word in the first variable has no matching word in the second variable at the overlap position, remove it.

Return **True** if the domain changed.  
Return **False** if no change occurred.

### Implement `ac3`
Enforce arc consistency across all variables.

If no arcs are given, begin with all arcs.

Process each arc using `revise`.  
If a revision occurs, add related arcs back to the queue.

If a domain becomes empty, return **False**.

### Implement `assignment_complete`
Return **True** if every crossword variable has a word assigned.

Return **False** otherwise.

### Implement `consistent`
Check whether the assignment satisfies all constraints.

Verify:
- Word lengths match the slot length
- Words are not repeated
- Overlapping letters match

Return **False** if any rule is violated.

### Implement `order_domain_values`
Return domain values ordered by the least constraining value rule.

Count how many values each word eliminates from neighboring variables.

Words that eliminate fewer options appear earlier.

### Implement `select_unassigned_variable`
Select a variable that is not assigned.

Choose the variable with the smallest domain.

If there is a tie, choose the variable with the most neighbors.

### Implement `backtrack`
Use recursive search to complete the crossword.

Steps:
1. Check if the assignment is complete.
2. Select an unassigned variable.
3. Try domain values in order.
4. Check if the assignment is consistent.
5. Continue recursively.

Return the assignment if a solution is found.

Return **None** if no solution exists.

---

# Troubleshooting Techniques

Use print statements to inspect domain values and assignments during execution.

Check that node consistency removes only incorrect word lengths.

Verify that overlapping characters are compared using the correct indices.

Test the solver with smaller structures to confirm each function works correctly.

If no solution is found, check whether domain reductions removed valid words.