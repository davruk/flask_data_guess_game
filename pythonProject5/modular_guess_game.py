from functions_guess_game_modular import play_game
from functions_guess_game_modular import top_scores


while True:
    choose = input("Would you like to A) play a new game, B) see the best scores, C) quit? ")

    if choose == "A":
        play_game()
    elif choose == "B":
        for score in top_scores():
            print(score)
    else:
        break
