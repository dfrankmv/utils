from ._multiton import *

P = ParamSpec("P")  # CATCH FUNCTION PARAMETER TYPES
R = TypeVar("R")    # CATCH FUNCTION RETURN TYPES

class Logger(Multiton):

    def __init__(self, name:str="default"):
        self.indent = 0
        self.millis = None
        self.tn_width = 0 # WIDTH OF THREAD NAME COLUMN
        self.fn_width = 0 # WIDTH OF FUNCTION NAME COLUMN
        self.blacklist = []

        mkdir("logs")

        self.logger = logging.getLogger(name)
        self.handler = TimedRotatingFileHandler(f"logs/{name}.log", when="midnight", interval=1, backupCount=32, encoding="utf-8")
        self.formatter = logging.Formatter("%(message)s")
        
        self.handler.setFormatter(self.formatter)
        self.handler.setLevel(logging.INFO)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self.handler)

    def msg(self, tag:str=None, msg:str=None, fun_name:str=None, millis:int=None):
        ms = millis if millis else current_millis()
        dt = millis2datetime(ms)
        tn = current_thread_name()
        obj, cls_name, _fun_name = get_caller_info(3) # FRAME_DEPTH = 3
        fun_name = fun_name if fun_name else _fun_name
        if cls_name:
            fn = f"{cls_name}[{id(obj)%100000}].{fun_name}()"
        else:
            if fun_name == "<module>":
                fn = "__main__"
            else:
                fn = f"{fun_name}()"
        self.fn_width = max(len(fn), self.fn_width)
        self.tn_width = max(len(tn), self.tn_width)
        _msg = f"{tag}: {msg}" if (tag and msg) else (tag or msg)
        return f"{dt} - {tn.ljust(self.tn_width)} - {fn.ljust(self.fn_width)} - {'│   '*self.indent}{_msg}"

    def info(self, tag:str=None, msg:str=None, fun_name:str=None):
        if tag not in self.blacklist:
            self.logger.info(self.msg(tag, msg, fun_name))



@overload
def log(tag:str=None, msg:str=None, fun_name:str=None) -> None: 
    """
    Inserts a log message with indentation if the caller is decorated with log.

    >>> class A:
    ...     def test1(self):
    ...         log("TEST_CAT", "Test msg 1")
    ...
    ...     @log
    ...     def test2(self)
    ...         log("TEST_CAT", "Test msg 2")

    >>> A().test()
        # FILE: default.log
        # 2025-08-10 10:46:48.125 - TN - MyObj[55216].test() - TEST_CAT: Test msg 1
        # 2025-08-10 10:46:48.130 - TN - MyObj[55216].test() - ┌── A.test()
        # 2025-08-10 10:46:48.146 - TN - MyObj[55216].info() - │   TEST_CAT: Test msg 2
        # 2025-08-10 10:46:48.147 - TN - MyObj[55216].test() - └── A.test() --> None
    """
    pass

@overload
def log(fun:Callable[P,R]) -> Callable[P,R]:
    """
    Logs the call of the function `fun` inserting an indent to the subsequent logs.

    >>> class A:
    ...     def test1(self):
    ...         log("TEST_CAT", "Test msg 1")
    ...
    ...     @log
    ...     def test2(self)
    ...         log("TEST_CAT", "Test msg 2")

    >>> A().test()
        # FILE: default.log
        # 2025-08-10 10:46:48.125 - TN - MyObj[55216].test() - TEST_CAT: Test msg 1
        # 2025-08-10 10:46:48.130 - TN - MyObj[55216].test() - ┌── A.test()
        # 2025-08-10 10:46:48.146 - TN - MyObj[55216].info() - │   TEST_CAT: Test msg 2
        # 2025-08-10 10:46:48.147 - TN - MyObj[55216].test() - └── A.test() --> None
    """
    pass

def log(p1=None, p2=None, p3=None):
    """
    As decorator: Logs the call of the function `fun` inserting an indent to the subsequent logs.

    As function: Inserts a log message with indentation if the caller is decorated with log.

    >>> class A:
    ...     @log
    ...     def test(self):
    ...         log("TEST_CAT", "Test msg")

    >>> A().test()
        # FILE: default.log
        # 2025-08-10 10:46:48.130 - TN - MyObj[55216].test() - ┌── A.test()
        # 2025-08-10 10:46:48.146 - TN - MyObj[55216].info() - │   TEST_CAT: Test msg
        # 2025-08-10 10:46:48.147 - TN - MyObj[55216].test() - └── A.test() --> None
    """
    _log = Logger()
    if callable(p1):
        fun = p1
        @wraps(fun)
        def wrapper(obj, *args, **kwargs) -> R:
            result = None
            # IF args[0] IS self, THE REST ARE ITS PARAMETERS
            if (len(args) > 0) and (obj is args[0]):
                args = args[1:]
            log("", f"┌── {fun.__qualname__.split('.')[0]}.{fun.__name__}()", fun.__name__)
            _log.indent += 1
            try:
                result = fun(obj, *args, **kwargs)
                return result
            except Exception as e:
                result = e
                raise
            finally:
                _log.indent -= 1
                log("", f"└── {fun.__qualname__.split('.')[0]}.{fun.__name__}() --> {result!r}", fun.__name__)
        return wrapper
    elif isinstance(p1, str) or isinstance(p2, str):
        tag, msg, fun_name = p1, p2, p3
        _log.info(tag, msg, fun_name)



if __name__ == "__main__":
    class A:
        def test1(self, myvar:int):
            log("TEST_CAT", f"1. myvar = {myvar}")
            return myvar

        @log
        def test2(self, myvar:int):
            log("TEST_CAT", f"2. myvar = {myvar}")
            return myvar*2

        @log
        def test3(self, myvar:int):
            log("TEST_CAT", f"3. myvar = {myvar}")
            log("BL_TEST", "This should not appear")
            raise Exception("This is an exception")


    Logger().blacklist.append("BL_TEST")
    a = A()

    r1 = a.test1(1)
    print(r1)

    r2 = a.test2(2)
    print(r2)

    a.test3(3)
    
    print(f"Logs created! Review the `default.log` file")

    """ 
    2025-10-23 04:18:17.760 - MainThread - log() - TEST_CAT: 1. myvar = 1
    2025-10-23 04:18:17.772 - MainThread - test2() - ┌── A.test2()
    2025-10-23 04:18:17.772 - MainThread - log()   - │   TEST_CAT: 2. myvar = 2
    2025-10-23 04:18:17.773 - MainThread - test2() - └── A.test2() --> 4
    2025-10-23 04:18:17.774 - MainThread - test3() - ┌── A.test3()
    2025-10-23 04:18:17.775 - MainThread - log()   - │   TEST_CAT: 3. myvar = 3
    2025-10-23 04:18:17.775 - MainThread - test3() - └── A.test3() --> Exception('This is an exception')
    """