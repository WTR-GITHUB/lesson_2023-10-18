# 1 --------------------------------------------
# def add_two_numbers(a: int, b: float) -> float:
#     print(a+b)

# add_two_numbers(5, 8)
# add_two_numbers(50, 81)
# add_two_numbers(500, 82134)

# 2 --------------------------------------------

def pow_of_number(a: float) -> float:
    return a**2

def make_string(text: str, no: int) -> str:
    return text + str(pow_of_number(no))

print(make_string("labas ", 5))
