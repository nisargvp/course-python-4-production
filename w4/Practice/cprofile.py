import cProfile

def my_func_2():
    for i in range(1000000):
        pass

def my_func_1():
    for i in range(3):
        my_func_2()

cProfile.run('my_func_1()')

# runctx:
import cProfile

def my_function():
    # code to be profiled
    pass

def another_function():
    # code to be profiled
    my_function()

def yet_another_function():
    # code to be profiled
    my_function()

profiler = cProfile.Profile()

# Profile my_function() when it is called directly or from another_function()
profiler.runctx('another_function()', globals(), locals())

# Print the profiling results
profiler.print_stats()


# dump_stats:
import cProfile
import pstats

def my_function():
    # code to be profiled
    pass

def another_function():
    # code to be profiled
    my_function()

def yet_another_function():
    # code to be profiled
     my_function()

profiler = cProfile.Profile()

# Profile my_function() when it is called directly or from another_function()
profiler.runctx('yet_another_function()', globals(), locals())
profiler.runctx('another_function()', globals(), locals())
# profiler.print_stats()

# Save the profiling results to a file
profiler.dump_stats('profile_results.prof')

# Load the profiling results from the file
stats = pstats.Stats('profile_results.prof')

# Print the profiling results, sorted by cumulative time
stats.sort_stats('cumulative').print_stats()

# sort_stats:
import cProfile
import pstats

def foo():
    for i in range(100000):
        pass

def bar():
    for i in range(1000000):
        pass

if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()

    foo()
    bar()

    pr.disable()

    # Sort by cumulative time spent in each function
    ps = pstats.Stats(pr).sort_stats('cumulative')
    ps.print_stats()
