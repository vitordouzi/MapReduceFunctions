from itertools import repeat, count, cycle, accumulate, chain, compress
from itertools import dropwhile, takewhile, islice, pairwise
from itertools import groupby as iter_groupby
from itertools import permutations, product, combinations, zip_longest
from functools import reduce
from operator import itemgetter
from heapq import merge, heappush, heappop
from multiprocessing import Pool, cpu_count

def imap(func, iterable, n_jobs=cpu_count()):
    with Pool(processes=n_jobs) as pool:
        for item in pool.imap(func, iterable):
            yield item
def imap_unordered(func, iterable, n_jobs=cpu_count()):
    with Pool(processes=n_jobs) as pool:
        for item in pool.imap_unordered(func, iterable):
            yield item
def flat(iterable):
    return chain.from_iterable(iterable)
def flat_map(func, iterable):
    return flat( map(func, iterable) )
def batch(iterable, batch_size, fillvalue=None):
    args = [iter(iterable)] * batch_size
    return zip_longest(*args, fillvalue=fillvalue)
def mapValues(func, iterable):
    return map(lambda x: (x[0], func(x[1])), iterable)
def mapKeys(func, iterable):
    return map(lambda x: (func(x[0]), x[1]), iterable)
def mmap(func, iterable):
    return map( lambda items: map(func, items), iterable )
def mmapValues(func, iterable):
    return map( lambda items: mapValues(func, items), iterable )
def mmapKeys(func, iterable):
    return map( lambda items: mapKeys(func, items), iterable )
def groupby(iterable):
    iterable = iter_groupby(iterable, itemgetter(0))
    iterable = mapValues(lambda item: map(itemgetter(1), item), iterable)
    return iterable
def merge_iterables(*iterables):
    # Initialize pointers as iterators
    pointers = [iter(it) for it in iterables]

    # Use a heap to keep track of the smallest item among the active pointers
    heap = []
    for i, it in enumerate(pointers):
        try:
            val = next(it)
            heappush(heap, (val, i))
        except StopIteration:
            pass

    # Loop until all pointers have been exhausted
    while heap:
        # Get the smallest item from the heap and yield its value
        smallest_val, smallest_idx = heappop(heap)
        yield smallest_val

        # Push the next value from the corresponding iterator onto the heap
        try:
            next_val = next(pointers[smallest_idx])
            heappush(heap, (next_val, smallest_idx))
        except StopIteration:
            pass

    # All iterators have been exhausted, so we're done
    return
