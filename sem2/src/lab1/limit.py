from functools import wraps


def call_limiter(limit):
    def class_decorator(cls):
        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value) and not (attr_name.startswith('__') and attr_name.endswith('__')):
                setattr(cls, attr_name, method_wrapper(attr_value, limit))
        return cls

    def method_wrapper(method, limit):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            if not hasattr(wrapper, 'call_count'):
                wrapper.call_count = 0

            if wrapper.call_count < limit:
                wrapper.call_count += 1
                return method(self, *args, **kwargs)
            else:
                print(f"Метод '{method.__name__}' достиг лимита в {limit} вызовов и больше не будет выполняться.")
                return None

        return wrapper

    return class_decorator

@call_limiter(limit=2)
class MyClass:
    def one(self):
        print("method_one")

    def two(self):
        print("method_two")

obj = MyClass()
obj.one()
obj.one()
obj.one()