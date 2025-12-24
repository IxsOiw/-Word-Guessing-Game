import random as rm

with open("words game /words.txt", "r") as file:
    words = [line.strip().lower() for line in file if line.strip()]

random_word = rm.choice(words)
positions = ["_"] * len(random_word)

attempts = 0
max_attempts = 12
used_letters = set()
remaining_letters = len(random_word)

print("------------------------------")
print("-                            -")
print("-  Word Guessing Game Start  -")
print("-                            -")
print("------------------------------")
print("The word has", len(random_word), "letters")
print(" ".join(positions))
print()

while remaining_letters > 0:

    if attempts >= max_attempts:
        print("You lost! The correct word was:", random_word)
        break

    letter = input("Enter a letter: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Enter ONE letter only!")
        continue

    if letter in used_letters:
        print("You already entered this letter")
        continue

    used_letters.add(letter)

    if letter in random_word:
        for i in range(len(random_word)):
            if random_word[i] == letter:
                positions[i] = letter
                remaining_letters -= 1

        print("Correct!")
    else:
        attempts += 1
        print("Incorrect! Remaining attempts:", max_attempts - attempts)

    print(" ".join(positions))
    print()

if remaining_letters == 0:
    print("YOU WON! The word was:", random_word)
