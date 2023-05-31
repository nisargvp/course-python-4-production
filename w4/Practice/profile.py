import profile
import time

def my_func():
    for _ in range(10):
        print(10)
        time.sleep(0.5)

profiler = profile.Profile()
profiler.run('my_func()')
profiler.print_stats()

# pstats.Stats.strip_dirs()
import cProfile, pstats

def some_function():
    for i in range(100000):
        pass

pr = cProfile.Profile()
pr.enable()

some_function()

pr.disable()
stats = pstats.Stats(pr)
stats.strip_dirs().sort_stats('cumulative').print_stats(10)

import cProfile, pstats

def some_function():
    for i in range(100000):
        pass

pr = cProfile.Profile()
pr.enable()

some_function()

pr.disable()
stats = pstats.Stats(pr)
stats.sort_stats('tottime').print_stats(10)