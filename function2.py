# Create a function that takes string as parameter and returns number of letters from that string.


# ------ su replace funcija trina tik trapus skaicius skaiciuoja ----------------------
text = input("Pleas enter string: ")

def count_letters(in_string: str):
    return len(in_string.replace(" ", ""))

print(count_letters(text))

# ------su isalpha funkcija renka tik raides---------------------------------------------

def count_letters_2(in_string: str):
    return len([char for char in in_string if char.isalpha()])

print(count_letters_2(text))