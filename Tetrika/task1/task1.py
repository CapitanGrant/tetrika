def strict(func):
    def wrapper(*args, **kwargs):
        lst_bool = []
        for k, v in func.__annotations__.items():
            if k != 'return':
                for i in args:
                    if not isinstance(i, v):
                        lst_bool.append(False)
                    else:
                        lst_bool.append(True)
        if all(lst_bool):
            return func(*args, **kwargs)
        else:
            raise TypeError(f"Аргумент не соответствует типу аннотации")

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
