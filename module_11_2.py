import inspect

class MyClass:

    def __init__(self):
        self.parameter = 1000
        self.fname = 'file.txt'

    def set_param(self, value):
        self.parameter = value

    def __add__(self, other):
        self.parameter += other.parameter
        return self

    def __str__(self):
        return str(self.parameter)

def show_all(*args):
    for j, _ in enumerate(*args):
        print(j, _)

def introspection_info(obj):
    info = {}
    '''
    members = inspect.getmembers(obj)
    for member in members:
        print(member, type(member))
    '''
    info['name'] = getattr(obj, '__name__', 'без имени')
    info['type'] = type(obj)
    info['callable'] = callable(obj)

    methods = [memb for memb, _ in inspect.getmembers(obj, inspect.isfunction)]
    attrs = [memb for memb, _ in inspect.getmembers(obj) if memb not in methods]

    #others = []

    print(f'Найдено {len(attrs)} аттрибутов: {attrs}')
    print(f'Найдено {len(methods)} функций: {methods}')
    #print(f'Найдено {len(others)} прочих элементов: {others}')

    info['attributes'] = attrs
    info['methods'] = methods

    info['module'] = inspect.getmodule(obj)

    return info


# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).
#
#
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
#
# Вывод на консоль:
# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
#
# Рекомендуется создавать свой класс и объект для лучшего понимания

def main():
    x = 42
    number_info = introspection_info(x)
    print(number_info)

    a = MyClass()
    # b = MyClass()
    a.set_param(2000)
    # c = a + b
    # show_all([a, b, c])

    print(introspection_info(MyClass))
    print(introspection_info(show_all))

    # print(inspect.ismethod(show_all))
    # print(inspect.isfunction(show_all))

if __name__ == '__main__':
    main()
    # print(dir())
