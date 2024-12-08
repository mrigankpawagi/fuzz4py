Return Code: 1
Stdout: SSL Error (invalid cert): not enough data: cadata does not contain a certificate (_ssl.c:4195)
SSL Error (large cert): not enough data: cadata does not contain a certificate (_ssl.c:4195)

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/844.py", line 91, in <module>
    context.load_verify_locations(cadata=None)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
TypeError: cafile, capath and cadata cannot be all omitted

