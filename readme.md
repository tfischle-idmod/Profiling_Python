# Profiling Python

## (Deterministic) Profiling
### cProfiler (C), profile(Python)
https://docs.python.org/3.7/library/profile.html
* cProfile is recommended for most users; it’s a C extension
* profile which is pure python and adds significant overhead
* can be run as module (-m) or as function

````python -m cProfile main.py````<br/>
<img src="cmd_cprofile_output.png" alt="command line output cProfile"/>

### PyCharm
* Needs PyCharm Professional
* Plots useful call <br/><br/>

[source code example call graph](main.py)<br/><br/>
<img src="profiling_main.png" alt="drawing" width="200"/>

### vprof
https://github.com/nvdv/vprof
* line debugger


## Memory usage
### mprof
Memory increase by line:
````python -m memory_profiler main_mem.py````
<img src="output_shell_mprof.png" alt="memory by line"/>

https://github.com/pythonprofilers/memory_profiler
* uses psutil module <br/><br/>
* @profile decorator

* created with <br/>
````mprof run --interval 0.001 main_mem.py````
````mprof plot````

<img src="mem_profile_main_mem.png" alt="memory usage over time"/>

## How does profiling work? 
### Python
In module sys, function ````setprofile()```` <br/>
"... The system’s profile function is called similarly to the system’s trace function (see settrace()),
but it is called with different events, for example it isn’t called for each executed line of code (only on call and
return, but the return event is reported even when an exception has been set). ..."
https://docs.python.org/3/library/sys.html#sys.setprofile

Similar there is a function ````settrace()```` <br/>
https://docs.python.org/3/library/sys.html#sys.settrace <br/>
eg. https://github.com/nvdv/vprof/blob/8898b528b4a6bea6384a2b5dbe8f38b03a47bfda/vprof/code_heatmap.py#L46


### C
https://github.com/python/cpython/blob/master/Lib/cProfile.py

https://github.com/python/cpython/blob/master/Modules/_lsprof.c, search for "_PyEval_SetProfile"

Python/C API Reference Manual - 8.2 Profiling and Tracing <br/>
https://users.cs.duke.edu/~raw/Python/api/profiling.html

## Statictical Profiling
# py-spy


# Other tools
### gprof2dot
* Open source
* needs Graphiz
* https://github.com/jrfonseca/gprof2dot
https://medium.com/@antoniomdk1/hpc-with-python-part-1-profiling-1dda4d172cdf

1. First of all, we need to tell the profiler to dump the collected data into a file:

````python3 -m cProfile -o output.pstats script.py````

2. Secondly, we run gprof2dot to generate a png image:

````gprof2dot -f pstats output.pstats | dot -Tpng -o output.png````
    

### pympler
Detailed information about size and lifetime of Python objects
https://pympler.readthedocs.io/en/latest/index.html#
    
