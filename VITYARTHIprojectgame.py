import random


def jumble_word(word):
    word_letters = list(word)
    random.shuffle(word_letters)
    return "".join(word_letters)


def play_game(words, hints):
    score = 0

    for i in range(len(words)):
        original_word = words[i]
        hint = hints[i]

        jumbled_word = jumble_word(original_word)

        print("\nJumbled Word:", jumbled_word.upper())
        print("Hint:", hint)

        chances = 3
        is_correct = False

        while chances > 0:
            guess = input("Your Guess: ").strip().lower()

            if guess == "exit":
                print("Game Stopped.")
                print("Your Score:", score)
                return score

            if guess == original_word.lower():
                print("Right Answer! Great job!")
                score = score + 10
                is_correct = True
                break
            else:
                chances = chances - 1

                if chances > 0:
                    print("Wrong answer! Chances left:", chances)

        if is_correct == False:
            print("Out of chances!")
            print("Correct word was:", original_word.upper())

    return score