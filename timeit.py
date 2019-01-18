import time

def timeit(func,a):
    start = time.time()
    ret = func(a)
    return (time.time() - start)
