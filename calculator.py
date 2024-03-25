import sys
import re

# NIE uczcie się na tym Pythona!

def add(*numbers: int|float) -> int|float:
    sum_val = 0
    for n in numbers:
        sum_val += n

    return sum_val

def subtract(a: int|float, b: int|float) -> int|float:
    return a - b

def multiply(*numbers: int|float) -> int|float:
    mul_val = 1
    for n in numbers:
        mul_val *= n

    return mul_val

def divide(a: int|float, b: int|float) -> float:
    return a / b


def split_by_operators(s:str) -> list[str]:
    return re.split(r'(\*|\-|\/|\+)', s)

def make_operation(eq_todo):
    operator = eq_todo[1]
    if operator == "+": return add(eq_todo[0], eq_todo[2])
    elif operator == "-": return subtract(eq_todo[0], eq_todo[2])
    elif operator == "\\": return divide(eq_todo[0], eq_todo[2])
    else: return multiply(eq_todo[0], eq_todo[2])

def main():
    eq = sys.argv[1]
    eq_todo = split_by_operators(eq)
    print(f"Got: {eq_todo}")

    result = make_operation(eq_todo)
    print(f"{eq} = {result}")


if __name__ == "__main__":
    main()
