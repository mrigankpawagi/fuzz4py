Return Code: 1
Stdout: Thread 130713105991232 received: 0, extra arg: 65
Thread 130713095505472 received: 1, extra arg: 68
Thread 130713085019712 received: 2, extra arg: 92
Thread 130713074533952 received: 3, extra arg: 28
Thread 130713064048192 received: 4, extra arg: 94
Time taken to call os.times(): 1.2073025573045015e-05, result: posix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4604764.3)
Error in os.times(): posix.times() takes no arguments (1 given)
Time taken to call os.times(): 4.129018634557724e-06, result: posix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4604764.3)
Error in os.times(): posix.times() takes no arguments (1 given)
Time taken to call os.times(): 2.363987732678652e-06, result: posix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4604764.3)
Error in os.times(): posix.times() takes no arguments (1 given)
Time taken to call os.times(): 1.962995156645775e-06, result: posix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4604764.3)
Error in os.times(): posix.times() takes no arguments (1 given)
Time taken to call os.times(): 1.6560079529881477e-06, result: posix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4604764.3)
Error in os.times(): posix.times() takes no arguments (1 given)

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/206.py", line 105, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/206.py", line 72, in main
    context.load_verify_locations(bad_cert)  # Example of loading bad certificate
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory

