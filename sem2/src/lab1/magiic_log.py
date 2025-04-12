import time
from functools import wraps


def class_logger(show_magic_methods=False):
    def class_decorator(classes):
        for attr_name, attr in classes.__dict__.items():
            if callable(attr):
                if not show_magic_methods and attr_name.startswith('__') and attr_name.endswith('__'):
                    continue
                setattr(classes, attr_name, _wrap_method(attr, attr_name))
        return classes
    return class_decorator

def _wrap_method(method, method_name):
    @wraps(method)
    def wrap (self, *arg, **kwargs):
        start_time = time.time()
        result = method(self, *arg, **kwargs)
        end_time = time.time()
        time_wrapped = end_time - start_time
        print(f'class: {self.__class__.__name__}, method: {method_name}, '
              f'arguments: {arg}, key arguments: {kwargs}, time: {time_wrapped}, '
              f'result {result}')
        return result
    return wrap


@class_logger(show_magic_methods=False)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Привет, меня зовут {self.name}!"

    def have_birthday(self):
        self.age += 1
        return f"С днём рождения! Теперь мне {self.age} лет."

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

person1 = Person("Алексей", 30)
person2 = Person("Мария", 25)

print(person1.greet())
print(person2.have_birthday())
print(person1)
print(person1 == person2)

