import random
import data

def generate_password():
    length = 12

    number_of_digits = random.randint(3, 10)

    number_of_letters = random.randint(2, length - number_of_digits)

    number_of_symbols = length - (number_of_digits + number_of_letters)

    a = [random.choice(data.numbers) for n in range(0, number_of_digits)]  
    b = [random.choice(data.letters) for n in range(0, number_of_letters)]
    c = [random.choice(data.symbols) for n in range(0, number_of_symbols)]

    a.extend(b)  # adding the 2 arrays seperately
    a.extend(c)

    random.shuffle(a)

    password = "".join(a)
    return password

