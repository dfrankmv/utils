from ..std import *

class CallbackList(List[Callable]):
    def append(self, f: Callable):
        if f not in self:
            super().append(f)

    def remove(self, f: Callable):
        if f in self:
            super().remove(f)
    
    def __call__(self, *args, **kwargs):
        for f in self:
            f(*args, **kwargs)

class EventsMeta(type):
    def __init__(cls, name:str, bases:tuple[type], dct:dict[str, Any]):
        super().__init__(name, bases, dct)
        original_init = dct.get("__init__")
        if original_init:
            def new_init(self, *args, **kwargs):
                Events.register_events(self)
                original_init(self, *args, **kwargs)
            cls.__init__ = new_init

class Fire:
    def __getattr__(self, attr):
        v = CallbackList()
        setattr(self, attr, v)
        return v

class Events(metaclass=EventsMeta):
    """
    Main class to manage event registration and firing.
    - Event handlers are methods starting with 'on_'.
    - Registered callbacks are stored in Events.fire.[event_name].

    >>> class Test(Events):
    ...    def __init__(self):
    ...        super().__init__()
    ...
    ...    def on_click(self, x, y):
    ...        print(f"Clicked at ({x},{y})")
    ...
    >>> t = Test()
    >>> Events.fire.on_click(10, 20) # "Clicked at (10,20)"
    """

    fire = Fire()

    def __init__(self):
        pass

    @classmethod
    def register_events(cls, obj:object, _cls:type=None):
        _cls = _cls if _cls else obj.__class__
        for base_cls in list(_cls.__mro__)[::-1]:
            for name, f in base_cls.__dict__.items():
                if callable(f) and name.startswith("on_"):
                    callbacks = getattr(cls.fire, name, CallbackList())
                    callbacks.append(getattr(_cls, name).__get__(obj, _cls))

if __name__ == "__main__":
    class A(Events):
        def __init__(self, x):
            # Events.register_events(self)
            self.x = x

        def on_test(self, w):
            print(f"x = {self.x + w}")

    a = A(1)
    Events.fire.on_test(2)