simbol = input("Please enter string with spec simbol: ")

def pick_spec_simb(in_string: str) -> str:
    spec_simb = ""
    chars = ["!","@","#","$","%","^","&","*","_","+","-"]
    for simb in in_string:
        for char in chars:
            if simb == char:
                spec_simb = str(spec_simb) + str(simb)
    return spec_simb

print(pick_spec_simb(simbol))