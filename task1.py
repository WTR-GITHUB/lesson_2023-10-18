def do_add(a:int, b:int) -> float:
    return float(a+b)

def do_sub(a:int, b:int) -> float:
    return float(a-b)

def do_mult(a:int, b:int) -> float:
    return float(a*b)

def do_div(a:int, b:int) -> float:
    return float(a/b)

def mind_f(a:int, b:int, c:str) -> str:
    return str(a)+c+str(b)

fisrts_num = int(input("Pleas enter a number 1: "))
second_num = int(input("Pleas enter a number 2: "))
simbol = input("Please enter simbols '-', '+', '*', '/': ")

while True:
    if simbol == "-":
        print(do_sub(fisrts_num, second_num))
        break
    elif simbol == "+":
        print(do_add(fisrts_num, second_num))
        break
    elif simbol == "*":
        print(do_mult(fisrts_num, second_num))
        break
    elif simbol == "/":
        print(do_div(fisrts_num, second_num))
        break
    else:
        print(f"What did you do?! {mind_f(fisrts_num, second_num, simbol)}")
        break