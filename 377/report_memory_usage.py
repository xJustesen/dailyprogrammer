import linecache
import os
import tracemalloc


def display_top(snapshot, key_type='lineno', limit=3):
    ''' This function displays which lines (top 3 by default) of code in a CODE BLOCK allocates the most total memory
    during the run-time of the CODE BLOCK. It should be used in the following way:

        tracemalloc.start() # Get the memory allocate before running CODE BLOCK

        /* CODE BLOCK */ # run CODE BLOCK

        snapshot = tracemalloc.take_snapshot() # Get the memory allocation of the CODE BLOCK
        display_top(snapshot) # report this in terminal

    Import the usual way:
            from report_memory_usage import * '''
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))
