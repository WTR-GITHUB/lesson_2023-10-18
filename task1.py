from typing import Union

def do_add(a:float, b:float) -> float:
    return float(a+b)

def do_sub(a:float, b:float) -> float:
    return float(a-b)

def do_mult(a:float, b:float) -> float:
    return float(a*b)

def do_div(a:float, b:float) -> float:
    return float(a/b)

def mind_f(a:float, b:float, c:str) -> str:
    return str(a)+c+str(b)

def check_execute(a:float, b:float, c: str):
    if c == "-":
        return print(do_sub(a, b))
    elif c == "+":
        return print(do_add(a, b))
    elif c == "*":
        return print(do_mult(a, b))
    elif c == "/":
        return print(do_div(a, b))
    else:        
        return print(f"What did you do?! {mind_f(a, b, c)}")

stop_cycle = True
while stop_cycle:
    first_number = float(input("Pleas enter a number 1: "))
    second_number = float(input("Pleas enter a number 2: "))
    simbol = input("Please enter simbols '-', '+', '*', '/': ")
    
    check_execute(first_number, second_number, simbol)
