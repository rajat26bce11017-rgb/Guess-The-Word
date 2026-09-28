import random

# Words aur unke hints ki simple list
words = ["Python", "computer", "keyboard", "variable", "internet", "program"]
hints = [
    "A popular coding language",
    "An electronic machine",
    "Used for typing",
    "Used to store data in code",
    "Global network of computers",
    "Set of instructions for computer",]


print("****************************************")
print("       WELCOME TO WORD GUESS GAME       ")
print("****************************************")
print("Rules:")
print("1. Guess the correct word.")
print("2. You have 3 chances for each word.")
print("3. Type 'exit' to quit anytime.")
print("----------------------------------------\n")

score = 0

# Loop through all words
for i in range(len(words)):
    original_word = words[i]
    hint = hints[i]

    # Word ke letters ko shuffle (jumble) karne ka simple logic
    word_letters = list(original_word)
    random.shuffle(word_letters)
    jumbled_word = "".join(word_letters)

    print("Jumbled Word:", jumbled_word.upper())
    print("Hint:", hint)

    chances = 3
    is_correct = False

    while chances > 0:
        guess = input("Your Guess: ").strip().lower()

        if guess == "exit":
            print("Game Stopped. Your Score:", score)
            break

        if guess == original_word.lower():
            print("Right Answer! Great job!\n")
            score = score + 10
            is_correct = True
            break
        else:
            chances = chances - 1
            if chances > 0:
                print("Wrong answer! Chances left:", chances)

    if guess == "exit":
        break

    if is_correct == False:
        print("Out of chances! Correct word was:", original_word.upper())
        print("----------------------------------------\n")

print("\n========================================")
print("              GAME OVER                 ")
print("Final Score:", score)
print("========================================")