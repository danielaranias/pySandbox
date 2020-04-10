
from functools import wraps



def PrintFuncDuritionTime(func:'put here function to check how long it takes'):
    """ Decorator for capturing the function elapsed time """

    import time
    
    #to capture the fun meta data
    @wraps(func)
    def elapsedTime(*args,**kargs):
        """
        printing the elapsing time of the input function 
        """
        start = time.perf_counter()
        res = func(*args,**kargs)
        end = time.perf_counter()
        print('{0} time is: {1}'.format(func.__name__,(end-start)))
        return res

    return elapsedTime


