import inspect

def get_caller_info(depth:int=2) -> tuple:
    """
    Retrieves information about the caller function.

    - depth = 0 -> Current function (`get_caller_info`)
    - depth = 1 -> The function/method that called `get_caller_info`
    - depth = 2 -> The function/method that called the function that called `get_caller_info`
    """
    outer_frame = inspect.getouterframes(inspect.currentframe())[depth]
    obj:object = outer_frame.frame.f_locals.get("self", None)
    fun_name = outer_frame.function
    cls_name = obj.__class__.__name__ if obj else ""
    return obj, cls_name, fun_name

if __name__ == "__main__":
    class A:
        def f(self):
            (obj, cls_name, fun_name) = get_caller_info()
            print(f"A.f() was called from {cls_name}.{fun_name}()")

    class B:
        def g(self):
            A().f()

    B().g()