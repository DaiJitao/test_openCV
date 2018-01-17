import abc
import six

def document_it(func):
    def new_function(*args, **kwargs):
        print '============================='
        print 'Running function in document_it:', func.__name__
        print 'Dange args; ', args
        print 'keyword args: ', kwargs
        result = func(*args, **kwargs)
        print 'result', result
        print '============================'
        return result
    return new_function

def square_it(func):
    def new_function(*args, **kwargs):
        print '*******************************'
        print 'Running function int square_it ', func.__name__
        print 'Dange args; ', args
        print 'keyword arges: ', kwargs
        result = func(*args, **kwargs)
        print '*******************************'
        return result * result
    return new_function

@square_it
@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)

@six.add_metaclass(abc.ABCMeta)
class Formatterclass(object):

    def __init__(self):
        pass
