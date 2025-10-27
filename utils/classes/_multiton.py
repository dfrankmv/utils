from ..helpers import *

class MultitonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # GET THE REAL SIGNATURE OF __init__ (IGNORE 'self')
        init = cls.__init__
        sig = inspect.signature(init)
        bound = sig.bind_partial(None, *args, **kwargs)  # None INSTEAD OF 'self'
        bound.apply_defaults()
        
        # CREATE KEY IGNORING 'self'
        key_items = list(bound.arguments.items())[1:]
        key_items = [(k, make_hashable(v)) for k, v in key_items]

        key = (cls, tuple(key_items))

        if key not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[key] = instance
            instance._initialized = False
        return cls._instances[key]
    
    def __init__(cls, name:str, bases:tuple[type], dct:dict[str, Any]):
        super().__init__(name, bases, dct)
        original_init = dct.get("__init__")
        if original_init:
            @wraps(original_init)
            def new_init(self, *args, **kwargs):
                if not getattr(self, "_initialized", False):
                    self._initialized = True
                    original_init(self, *args, **kwargs)
            dct["__init__"] = new_init

class Multiton(metaclass=MultitonMeta):
    pass

if __name__ == "__main__":
    class Test1(Multiton):
        def __init__(self, p:str):
            print(f"> {p}")

    class Test2(Multiton):
        def __init__(self, p:str):
            print(f">> {p}")

    a = Test1("a")
    b = Test1("b")
    c = Test1("a")  # init is not called again
    d = Test1("b")  # init is not called again
    A = Test2("a")
    B = Test2("b")
    C = Test2("a")  # init is not called again
    D = Test2("b")  # init is not called again

    print(a is b)
    print(a is c)
    print(b is c)
    print(b is d)
    print(a is A)
    print(A is B)
    print(A is C)