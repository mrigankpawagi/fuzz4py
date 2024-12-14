import os
import random

script_path = os.path.dirname(os.path.realpath(__file__))

# read the grammar file and load the grammar
with open(os.path.join(script_path, "python.lark")) as f:
    grammar_lines = f.readlines()

# remove empty lines and lines starting with '//' or '%'
def keep_line(line: str) -> bool:
    line = line.strip()
    return line and not line.startswith("//") and not line.startswith("%")

grammar_lines = list(filter(keep_line, grammar_lines))

def random_grammar_excerpt(n: int) -> str:
    """
    Return a random excerpt of the grammar of length n.
    """
    assert n > 0, "n must be greater than 0"

    # choose a random line from the grammar where a rule begins
    candidate_line_indices = [i for i, line in enumerate(grammar_lines) if not line[0].isspace()]

    # choose a random line from the candidate lines
    line_index = random.choice(candidate_line_indices)

    # select the next n lines
    next_line_indices = [i for i in candidate_line_indices if i > line_index]
    if not next_line_indices: next_line_index = len(grammar_lines)
    else:
        next_line_indices_clip = [i for i in candidate_line_indices if i >= line_index + n]
        if next_line_indices_clip: next_line_index = min(next_line_indices_clip)
        else: next_line_index = len(grammar_lines)

    return "".join(grammar_lines[line_index:next_line_index])
