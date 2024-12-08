Return Code: 1
Stdout: 
Stderr:   File "/home/mrigankp/fuzz4py/fuzz4py/inputs/999.py", line 26
    data[i] *= 2  if random.random() > 0.2 else data[i] -=1  # Random operation
                                                        ^^
SyntaxError: invalid syntax

