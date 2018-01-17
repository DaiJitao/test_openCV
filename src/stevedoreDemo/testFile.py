
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print self.calls, self.func.__name__
        self.func(*args)

@tracer
def spam(a, b, c):
    print "a=",a , "b=",b, "c=",c

def myfun():
    print "myfun() called"

myfun()