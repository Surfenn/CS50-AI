# Week 2 PagerankProject
 
1. Introduction

This project implements Google’s PageRank algorithm to rank web pages based on how they link to one another. Instead of analyzing the content of a page, PageRank measures importance using link structure. A page becomes more important if other important pages link to it.

The program reads a directory of HTML files, builds a representation of how the pages connect, and computes PageRank values for each page. These values represent the probability that a random web surfer would be on that page at any moment. The final results form a probability distribution where all values sum to 1.

Two methods are used to calculate PageRank: a sampling method based on a random surfer model and an iterative method based on a mathematical formula.

2. Planning Phase

The planning stage focused on understanding how PageRank works mathematically and how to translate it into code. The main objective was to design a system that could compute PageRank using both simulation and iteration while following the project constraints.

The program had to use Python 3.12 and only standard library modules. Only three functions were allowed to be modified: transition_model, sample_pagerank, and iterate_pagerank. All probability distributions needed to sum to 1, and the iterative method needed to stop once changes were smaller than 0.001.

Special attention was given to edge cases, such as pages with no outgoing links and disconnected page structures.

3. Requirements Analysis

The project required implementing three core functions.

The transition_model function returns a probability distribution showing which page a random surfer will visit next. With probability d, the surfer follows a link from the current page. With probability (1 − d), the surfer jumps to any page in the corpus. If a page has no outgoing links, it is treated as linking to all pages equally.

The sample_pagerank function estimates PageRank values by simulating a random surfer for a large number of steps. It tracks how many times each page is visited and converts those counts into probabilities.

The iterate_pagerank function calculates PageRank using the formula:

PR(p) = (1 − d) / N + d × Σ (PR(i) / NumLinks(i))

This function repeatedly updates rank values until the change between iterations is no greater than 0.001.

4. System Design

The system is modular. The provided crawl() function builds the corpus by reading HTML files and extracting links. The transition model calculates probability distributions. The sampling function simulates movement between pages. The iterative function applies the PageRank formula until convergence. The main function runs both methods and prints the results.

The main data structure used is a dictionary. The corpus is stored as {page: set_of_links}, and PageRank results are stored as {page: probability}. This structure makes it easy to access and update values while keeping the program organized.

5. Implementation Details

The transition model first calculates the total number of pages. If the current page has links, each page receives a base probability of (1 − d) / N. Linked pages then receive an additional share of the damping factor. If there are no outgoing links, each page receives equal probability.

The sampling method starts from a random page and repeatedly chooses the next page based on the transition model. It counts visits and divides by the total number of samples to produce PageRank values. As the number of samples increases, the estimate becomes closer to the true value.

The iterative method starts by assigning each page a rank of 1 / N. It then updates each page’s rank based on the ranks of pages linking to it. If a page has no outgoing links, it is treated as linking to all pages. The process continues until the maximum change in rank is 0.001 or less.

6. Testing Strategy

Testing focused on verifying that probability distributions always sum to 1 and that pages with no outgoing links are handled correctly. The results from the sampling and iterative methods were compared to confirm they were close in value.

Edge cases such as single-page corpora and disconnected structures were also tested. The final implementation was checked using check50 and style50 to confirm correctness.

7. Risk Analysis

One possible issue was floating-point precision during iteration. This was handled by using a convergence threshold of 0.001. Another risk was incorrect dictionary structure, which could cause grading errors. Following the specification carefully avoided this problem.

8. Conclusion

This project shows two ways to compute PageRank: simulation and iteration. The sampling method models user behavior, while the iterative method applies a mathematical formula until values stabilize.

Both approaches reflect the idea that a page’s importance depends on the importance of the pages linking to it. Through this project, I developed a clearer understanding of probability distributions, Markov chains, and convergence in iterative algorithms.

The final program correctly calculates PageRank values for any valid corpus of web pages.