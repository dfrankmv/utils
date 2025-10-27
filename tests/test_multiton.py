from utils import *

# This dict indicates the number of times the constructors are called
init_count = {"A":0, "B":0}

@pytest.fixture(autouse=True)
def reset():
    global init_count
    init_count = {"A":0, "B":0}
    A._instances = {}
    B._instances = {}

class A(Multiton):
    def __init__(self, x:int, y:int=None):
        init_count["A"] += 1

class B(Multiton):
    def __init__(self, x:int, y:int=None):
        init_count["B"] += 1

def test_keep_original_constructors():
    """ 
    Ensure `Multiton` does not alter the original constructors on first call.
    """
    a = A(1) # A.__init__(1) is executed
    b = B(1) # B.__init__(1) is executed
    assert init_count == {"A": 1, "B": 1}

def test_run_constructor_once():
    """ 
    `__init__` should run only on the first instantiation with the same parameters.
    """
    a1 = A(1) # A.__init__(1) is executed
    a11 = A(1) # A.__init__(1) is skipped
    a111 = A(1) # A.__init__(1) is skipped
    assert init_count == {"A": 1, "B": 0}

def test_same_classes_same_params_same_object():
    """ 
    Instances of the same class with identical parameters should return the same object.
    """
    a1 = A(1) # a1 is created
    a11 = A(1) # a1 is returned
    a111 = A(1) # a1 is returned
    b1 = B(1) # b1 is created
    b11 = B(1) # b1 is returned
    b111 = B(1) # b1 is returned
    assert a1 is a11
    assert a1 is a111
    assert b1 is b11
    assert b1 is b111
    assert a1 is not b1

def test_diff_classes_diff_params_diff_objects():
    """ 
    Instances from different classes should always be different objects.
    """
    a1 = A(1) # a1 is created
    b1 = B(1) # b1 is created
    assert a1 is not b1
    assert init_count == {"A": 1, "B": 1}

def test_same_class_diff_params_diff_objects():
    """ 
    Same class but different parameters should yield distinct instances.
    """
    a1 = A(1)
    a2 = A(2)
    assert a1 is not a2
    assert init_count == {"A": 2, "B": 0}

def test_multi_params():
    """ 
    Different parameter combinations should yield unique instances per combination.
    """
    a1 = A(1, 11) # a1 is created
    a11 = A(1, 11) # a1 is returned
    a2 = A(1, 22) # a2 is created
    a22 = A(1, 22) # a2 is returned
    a3 = A(3, 22) # a3 is created
    a33 = A(3, 22) # a3 is returned
    assert a1 is a11
    assert a2 is a22
    assert a3 is a33
    assert init_count == {"A": 3, "B": 0}


def test_positional_args():
    """ 
    Positional and keyword arguments representing the same values should yield the same instance.
    """
    a1 = A(1, 11) # a1 is created
    a11 = A(y=11, x=1) # a1 is returned
    assert a1 is a11
    assert init_count == {"A": 1, "B": 0}

def test_thread_safety():
    """ 
    Concurrent calls with identical parameters should return a single shared instance.
    """
    def make_a(i):
        return A(1)
    with concurrent.futures.ThreadPoolExecutor() as ex:
        instances = list(ex.map(make_a, range(10)))
    assert len({id(r) for r in instances}) == 1

def test_keyword_order_irrelevant():
    """
    Keyword argument order should not affect instance identity.
    """
    a1 = A(x=1, y=11)
    a2 = A(y=11, x=1)
    assert a1 is a2
    assert init_count == {"A": 1, "B": 0}