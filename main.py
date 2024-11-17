from datetime import datetime
#task1
class CreationTimeMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance._creation_time = datetime.now()
        return instance
class MyClass(metaclass=CreationTimeMeta):
    pass
obj = MyClass()
print(obj._creation_time)

#task2
class ClassInfoMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        def get_class_info(cls):
            return dir(cls)
        setattr(cls, 'get_class_info', classmethod(get_class_info))
class MyClass(metaclass=ClassInfoMeta):
    def method(self):
        pass

obj = MyClass()
print(MyClass.get_class_info())

#task3
class ImmutableAttributesMeta(type):
    def __setattr__(cls, name, value):
        if name in cls.__dict__:
            raise AttributeError(f"Неможливо змінити атрибут {name}")
        super().__setattr__(name, value)

class MyClass(metaclass=ImmutableAttributesMeta):
    def __init__(self, value):
        self.value = value

obj = MyClass(10)
print(obj.value)
try:
    obj.value = 20
except AttributeError as e:
    print(e)

#task4
class RestrictedInheritanceMeta(type):
    def __init__(cls, name, bases, dct):
        if RestrictedInheritanceMeta in [base.__class__ for base in bases]:
            raise TypeError(f"Неможливо наслідувати від забороненого класу")
        super().__init__(name, bases, dct)

class BaseClass(metaclass=RestrictedInheritanceMeta):
    pass

class AllowedClass(BaseClass):
    pass

try:
    class RestrictedClass(RestrictedInheritanceMeta):
        pass
except TypeError as e:
    print(e)


