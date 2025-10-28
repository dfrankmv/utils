from utils import *

counter = {}

@pytest.fixture(autouse=True)
def reset():
    global counter
    counter = {}

@daemon
def t_produce(name:str):
    counter[name] = counter.get(name, 0) + 1

def test_return_thread():
    a = t_produce("A")
    assert isinstance(a, Thread)

def test_run_in_parallel():
    a = t_produce("A")
    b = t_produce("B")
    a.join()
    b.join()
    assert counter == {"A":1,"B":1}