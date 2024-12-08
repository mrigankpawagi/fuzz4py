Return Code: 1
Stdout: Thread 135332477535808 received: 0, extra arg: 60
Thread 135332467050048 received: 1, extra arg: 12
Thread 135332456564288 received: 2, extra arg: 32
Thread 135332446078528 received: 3, extra arg: 75
Thread 135332435592768 received: 4, extra arg: 20
Time taken to call os.times(): 1.2301024980843067e-05, result: posix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4610663.53)
Error in os.times(): posix.times() takes no arguments (1 given)
Time taken to call os.times(): 5.382986273616552e-06, result: posix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4610663.53)
Error in os.times(): posix.times() takes no arguments (1 given)
Time taken to call os.times(): 2.193031832575798e-06, result: posix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4610663.53)
Error in os.times(): posix.times() takes no arguments (1 given)
Time taken to call os.times(): 1.9939616322517395e-06, result: posix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4610663.53)
Error in os.times(): posix.times() takes no arguments (1 given)
Time taken to call os.times(): 1.9239960238337517e-06, result: posix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4610663.53)
Error in os.times(): posix.times() takes no arguments (1 given)

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/206.py", line 105, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/206.py", line 72, in main
    context.load_verify_locations(bad_cert)  # Example of loading bad certificate
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory

