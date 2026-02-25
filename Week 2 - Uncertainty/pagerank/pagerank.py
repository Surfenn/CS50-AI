import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.
    """

    distribution = {}
    total_pages = len(corpus)
    links = corpus[page]

    if len(links) == 0:
        for p in corpus:
            distribution[p] = 1 / total_pages
        return distribution

    for p in corpus:
        distribution[p] = (1 - damping_factor) / total_pages

    link_probability = damping_factor / len(links)
    for linked_page in links:
        distribution[linked_page] += link_probability

    return distribution

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages.
    """
    visit_counts = {}
    for page in corpus:
        visit_counts[page] = 0

    current_page = random.choice(list(corpus.keys()))
    visit_counts[current_page] += 1

    for i in range(1, n):

        model = transition_model(corpus, current_page, damping_factor)

        pages = list(model.keys())
        probabilities = list(model.values())

        current_page = random.choices(
            population=pages,
            weights=probabilities,
            k=1
        )[0]

        visit_counts[current_page] += 1

    pagerank = {}
    for page in visit_counts:
        pagerank[page] = visit_counts[page] / n

    return pagerank

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    total_pages = len(corpus)

    pagerank = {}
    for page in corpus:
        pagerank[page] = 1 / total_pages

    converged = False

    while not converged:

        new_pagerank = {}
        converged = True

        for page in corpus:

            rank_sum = 0

            for other_page in corpus:
                links = corpus[other_page]

                if len(links) == 0:
                    rank_sum += pagerank[other_page] / total_pages

                elif page in links:
                    rank_sum += pagerank[other_page] / len(links)

            new_rank = ((1 - damping_factor) / total_pages) + \
                       (damping_factor * rank_sum)

            new_pagerank[page] = new_rank

        # Check convergence
        for page in pagerank:
            if abs(new_pagerank[page] - pagerank[page]) > 0.001:
                converged = False

        pagerank = new_pagerank

    return pagerank


if __name__ == "__main__":
    main()
