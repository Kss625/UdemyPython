import random

word_list = ["UDEMY", "APPMILLERS", "PYTHON"]
secret_word = random.choice(word_list)
blanks = []
for _ in range(len(secret_word)):
    blanks.append("_")
print(blanks)

lives = 6

guessed_letter = []
end_game = False
while not end_game:
    guess = input("Guess a letter:").upper()

    if guess in guessed_letter:
        print("You have already Guessed The Letter")
        continue
    else:
        guessed_letter.append(guess)
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if guess == letter:
            blanks[position] = letter
    if guess not in secret_word:
        lives = lives - 1
    if lives == 0:
        print("You Lose")
    print(blanks)
    if "_" not in blanks:
        end_game = True
