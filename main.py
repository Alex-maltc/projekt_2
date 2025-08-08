"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Aleksei Maltcev
email: alexmal@post.cz
"""



import random

# Generování tajného čísla (nezačíná nulou)
def generate_secret_number():
    digits = list("123456789")  # první číslice nesmí být 0
    first_digit = random.choice(digits)
    digits = list("0123456789")
    digits.remove(first_digit)
    random.shuffle(digits)
    return first_digit + ''.join(digits[:3])

# Vyhodnocení bulls a cows
def get_bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

# Herní smyčka
def play_game():
    print("Hi there!!")
    print("I've generated a random 4 digit number for you. Let's play a bulls and cows game.")
    print("a 'cows' (správné číslo, špatná pozice).")
    print("Zadej 'exit' pro ukončení.\n")

    secret = generate_secret_number()
    attempts = 0

    while True:
        guess = input("Enter a number: ")

        if guess.lower() == 'exit':
            print(f"Tajné číslo bylo: {secret}")
            break

        # Validace vstupu
        if not guess.isdigit():
            print("Chyba: Zadání obsahuje nečíselné znaky.")
            continue

        if len(guess) != 4:
            print("Chyba: Zadej přesně 4 čísla.")
            continue

        if len(set(guess)) != 4:
            print("Chyba: Číslice se nesmí opakovat.")
            continue

        if guess[0] == '0':
            print("Chyba: Číslo nesmí začínat nulou.")
            continue

        # Správné zadání → pokračuj
        attempts += 1
        bulls, cows = get_bulls_and_cows(secret, guess)
        print(f"{bulls} bulls, {cows} cows")

        if bulls == 4:
            print(f"Gratuluji! Uhodl jsi tajné číslo {secret} za {attempts} pokusů.")
            break

# Spuštění hry
if __name__ == "__main__":
    play_game()
