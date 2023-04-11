from itertools import islice
from functools import partial


l = [1, 2, 3, 4, 5, 6]
l2 = [1, 2, 3, 4, 5, 6, 7]

def take(iterable:list, n:int) ->list:
    return list(islice(iterable, n))


def chunked(iterable:list, n:int, strict:bool=False):
    iterator = iter(partial(take, iter(iterable), n), [])
    if strict:
        if n is None:
            raise ValueError("n can't be None when strict is True")
        if len(iterable) % n == False:
            return iterator
        elif len(iterable) % n == True : 
            raise ValueError("iterator is not divisible by n")     # تعداد لیست بر عدد ورودی بخش پذیر نیست 

    else:
        return iterator



print(list(chunked(l2, 3, strict=False)))
