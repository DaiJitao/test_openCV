
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
plt.plot(randn(50).cumsum(), "k--")
_ = ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))

class Test(object):
    x = 11
    def __init__(self, _x):
        self._x = _x
        print("Test.__init__")

    @classmethod
    def class_method(cls):
        print "class_method"

    @staticmethod
    def static_method():
        print "static_method"

    @classmethod
    def getPt(cls):
        cls.class_method()
        cls.static_method()
        print cls


if __name__=="__main__":
    Test.class_method()
    Test.static_method()
    Test.getPt()