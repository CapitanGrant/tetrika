from task1.solution import strict, sum_two

import pytest


# Тестируемая функция с декоратором
@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def concat_strings(s1: str, s2: str) -> str:
    return s1 + s2


@strict
def greet(name: str, age: int, is_active: bool) -> str:
    return f"{name}, {age}, active: {is_active}"


### Тесты для корректных случаев
def test_correct_int_args():
    assert sum_two(1, 2) == 3


def test_correct_str_args():
    assert concat_strings("Hello, ", "world!") == "Hello, world!"


def test_correct_mixed_args():
    assert greet("Alice", 25, True) == "Alice, 25, active: True"


### Тесты для ошибочных случаев
def test_incorrect_first_arg():
    with pytest.raises(TypeError):
        sum_two(1.5, 2)  # Первый аргумент не int


def test_incorrect_second_arg():
    with pytest.raises(TypeError):
        sum_two(1, "2")  # Второй аргумент не int


def test_incorrect_both_args():
    with pytest.raises(TypeError):
        sum_two("1", 2.5)  # Оба аргумента неверного типа


def test_incorrect_kwargs():
    with pytest.raises(TypeError):
        concat_strings(s1=123, s2="world")  # s1 не str


def test_mixed_correct_and_incorrect():
    with pytest.raises(TypeError):
        greet("Bob", "25", False)  # age должен быть int


### Дополнительные тесты
def test_no_annotation_no_error():
    @strict
    def untyped_func(a, b):
        return a + b

    assert untyped_func(1, 2) == 3  # Должно работать без аннотаций
    assert untyped_func("a", "b") == "ab"


def test_return_annotation_not_checked():
    @strict
    def bad_return(a: int) -> str:
        return a  # Возвращает int вместо str, но это не должно вызывать ошибку

    assert bad_return(123) == 123  # Декоратор не проверяет возвращаемое значение


if __name__ == "__main__":
    pytest.main(["-v"])