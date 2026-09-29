from words import words, hints
from game import play_game


print("                                        ")
print("       WELCOME TO WORD GUESS GAME")
print("                                         ")

print("Rules:")
print("1. Guess the correct word.")
print("2. You have 3 chances for each word.")
print("3. Type 'exit' to quit anytime.")
print("                                     ")

final_score = play_game(words, hints)

print("\n----------------------------------------")
print("              GAME OVER")
print("                                           ")
print("Final Score:", final_score)
print("                                            ")