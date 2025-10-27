from utils import *

""" 
Testing Events using `Events` class as parent class
"""

results = {"A":0, "B":0, "C":0}

def reset():
    global results
    results = {"A":0,"B":0,"C":0}
    Events.fire = Fire()

class A(Events):
    def __init__(self, x:int):
        results["A"] += x

    def on_test(self, v:int):
        results["A"] += v

class B(A):
    def __init__(self, x:int):
        results["B"] += x

    def on_test(self, v:int):
        results["B"] += v

class C(B):
    def __init__(self, x:int):
        B.__init__(self, x)
        results["C"] += x

    def on_test(self, v:int):
        results["C"] += v


def test_fire_one():
    """
    The object `a=A(1)` registers the `a.on_test` event.  
    """
    reset()
    a = A(1)
    Events.fire.on_test(5) # a.on_test(5) is executed
    assert results == {"A":6, "B":0, "C":0}

def test_fire_multiple():
    """
    The objects `a1=A(1)`, `a10=A(10)`, and `a100=A(100)` register 
    `a1.on_test`, `a10.on_test` and `a100.on_test` events.
    """
    reset()
    a1 = A(1) # results["A"] = 1
    a10 = A(10) # results["A"] = 11
    a100 = A(100) # results["A"] = 111
    Events.fire.on_test(7) # a1.on_test(7), a10.on_test(7), and a100.on_test(7) are executed
    assert results == {"A":1 + 10 + 100 + 7 + 7 + 7, "B":0, "C":0}

def test_fire_child():
    """ 
    B inherits from A but it doesn't matter, the object `b=B(2)` registers
    `b.on_test` event once.
    """
    reset()
    Events.fire = Fire()
    b = B(2)
    Events.fire.on_test(5) # b.on_test(2) is executed
    assert results == {"A":0, "B":7, "C":0}

    a = A(1) # results = {"A":1, "B":7, "C":0}
    Events.fire.on_test(7) # a.on_test(7) and b.on_test(7) are executed
    assert results == {"A":1 + 7, "B":7 + 7, "C":0}

def test_multiple_constructor():
    """ 
    In this test, the object `c=C(3)` is created. `C.__init__` makes 
    `results["C"]=3` and registers the `c.on_test` event, also `B.__init__` 
    makes `results["B"]=3`and is trying to register the `c.on_test` event 
    but it is already registered so it will be skipped. 
    """
    reset()
    Events.fire = Fire()
    c = C(3)
    Events.fire.on_test(5) # c.on_test(5) is executed
    assert results == {"A":0, "B":3, "C":3 + 5}