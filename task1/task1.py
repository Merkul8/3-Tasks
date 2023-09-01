
def strict(func):
    def wrapper(*args, **kwargs):
        res_types = []
        arg_values = list(args) + list(kwargs.values())
        for value in arg_values:
            # Узнаем типы каждого параметра
            res_types.append(type(value))
        # Преобразуем типы в set(), чтобы узнать их уникальность
        if len(set(res_types)) != 1:
            raise TypeError('Ошибка типов')
        # Вызываем исходную функцию и возвращаем её результат
        return func(*args, **kwargs)
    
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

# print(sum_two(1, 2))    # >>> 
print(sum_two(1, 'Хай'))  # >>> TypeError
