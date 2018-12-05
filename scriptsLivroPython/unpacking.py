def unpacking_experiment(*args):
    arg1 = args[0]
    arg2 = args[1]
    others = args[2:]
    print(arg1)
    print(arg2)
    print(others)

unpacking_experiment(1, 2, 3, 4, 5, 6, 7)