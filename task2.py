simbol = input("Please enter string: ")

def add_simb(text: str) -> list:
    my_list = []
    for item in text:
        my_list.append(item + "$")
    return my_list

print(add_simb(simbol))
