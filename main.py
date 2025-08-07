"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Petr Svetr
email: petr.svetr@gmail.com
"""



import random

# 1. Generování tajného čísla
def generate_secret_number():
    digits = list("0123456789")
    random.shuffle(digits)
    return ''.join(digits[:4])

# 2. Funkce pro vyhodnocení bulls a cows
def get_bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

# 3. Hlavní smyčka hry
def play_game():
    print("Vítej ve hře 'Cows and Bulls'!")
    print("Hádej 4 různá čísla. Po každém pokusu ti řeknu, kolik máš 'bulls' (správné číslo a pozice)")
    print("a 'cows' (správné číslo, špatná pozice).")
    print("Zadej 'exit' pro ukončení.\n")

    secret = generate_secret_number()
    attempts = 0

    while True:
        guess = input("Zadej svůj tip (4 různá čísla): ")
        
        if guess.lower() == 'exit':
            print(f"Tajné číslo bylo: {secret}")
            break

        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Neplatný vstup. Zadej přesně 4 různá čísla.")
            continue

        attempts += 1
        bulls, cows = get_bulls_and_cows(secret, guess)
        print(f"{bulls} bulls, {cows} cows")

        if bulls == 4:
            print(f"Gratulace! Uhodl jsi číslo {secret} za {attempts} pokusů.")
            break
