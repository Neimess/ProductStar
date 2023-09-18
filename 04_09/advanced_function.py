# 1. Напишите функцию, которая принимает список строк в качестве аргументов и возвращает новый список, содержащий только строки, 
# являющиеся палиндромами. Палиндром — это слово, которое одинаково читается как вперед так и назад (например, «racecar», «level», «deified»). 
# Используйте лямбда-функцию, чтобы проверить, является ли строка палиндромом.

# ​​2. Напишите генератор-функцию, которая генерирует последовательность Коллатца для заданного начального числа. 
# Последовательность генерируется путем многократного применения правила к каждому числу в последовательности: если число четное, разделите его на 2, 
# иначе умножьте его на 3 и добавьте 1. Последовательность завершается, когда достигает числа 1. Используйте замыкания для хранения текущего номера в последовательности.

# 3. Напишите функцию, которая принимает на вход список целых чисел и возвращает новый список, 
# в котором каждое целое число заменено квадратным корнем, округленным до ближайшего целого числа. 
# Используйте аргументы с ключевыми словами, чтобы пользователь мог указать направление округления (вверх или вниз). 
# Используйте декоратор для определения времени выполнения функции.
import time
import math

def execution_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"Function {function.__name__} took {end_time - start_time} seconds to run")
        return result
    return wrapper

def palindromes(lst):
    words = filter(lambda x: x==x[::-1], lst)
    return list(words)

def collatz_closure(num):
    current = num
    def inner():
        nonlocal current
        while current != 1:
            yield current
            current = current // 2 if current % 2 == 0 else current * 3 + 1
        yield current
    return inner
        
def collatz_generator(num):
    current = num
    while current != 1:
        yield current
        current = current // 2 if current % 2 == 0 else current * 3 + 1
    yield current    

@execution_time    
def calculate_square_roots(nums: list, rounding_direction="round"):
    
    if rounding_direction == "round":
        return list(map(lambda x: round(math.sqrt(x)), nums))
    elif rounding_direction == "up":
        return list(map(lambda x: math.ceil(math.sqrt(x)), nums))
    elif rounding_direction == "down":
        return list(map(lambda x: math.floor(math.sqrt(x)), nums))
    else:
        raise ValueError("Unknown value key for rounding_direction")
    
def test_palidromes(lst: list):
    print(palindromes(lst))
    
def test_collatz_closure(num):
    get_collatz = collatz_closure(num)
    for i in get_collatz():
        print((i))

def test_collatz(num):
    for i in collatz_generator(num):
        print(i)

def test_square(lst:list):
    print(calculate_square_roots(lst, "down"))
    
test_palidromes(["racecar", "level", "deified"])
test_collatz_closure(18)
test_collatz(18)
test_square([i for i in range(1, 10)])
