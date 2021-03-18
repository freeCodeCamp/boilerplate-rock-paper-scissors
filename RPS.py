# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

guessed = []


def player(prev_play, opponent_history=[]):
    global guessed
    third = 1 / 3
    opponent_history.append(prev_play)

    markov_df = {}
    # NEXT BOT OUTPUT   R   ,   P  ,   S
    markov_df["PR"] = [third, third, third]
    markov_df["PP"] = [third, third, third]
    markov_df["PS"] = [third, third, third]
    markov_df["RR"] = [third, third, third]
    markov_df["RP"] = [third, third, third]
    markov_df["RS"] = [third, third, third]
    markov_df["SR"] = [third, third, third]
    markov_df["SP"] = [third, third, third]
    markov_df["SS"] = [third, third, third]

    if len(guessed) <= 4:
        guess = random.choice(["R", "P", "S"])
        guessed.append(guess)
    elif len(opponent_history) >= 3:
        for i in range(len(opponent_history) - 1):
            key = guessed[i] + opponent_history[i]
            if len(key) < 2:
                key = guessed[i] * 2
            next_move = opponent_history[i + 1]
            if next_move == "R":
                markov_df[key][1] += third
                markov_df[key][0] -= third
                markov_df[key][2] -= third
            elif next_move == "P":
                markov_df[key][2] += third
                markov_df[key][1] -= third
                markov_df[key][0] -= third
            elif next_move == "S":
                markov_df[key][0] += third
                markov_df[key][1] -= third
                markov_df[key][2] -= third

        last_key = guessed[-2] + opponent_history[-1]
        if len(last_key) < 2:
            last_key = guessed[-2] * 2
        probR = markov_df[last_key][0]
        probP = markov_df[last_key][1]
        probS = markov_df[last_key][2]
        maxed_prob = max(probR, probP)
        maxed_prob = max(maxed_prob, probS)

        if maxed_prob == probR:
            guess = "R"
        elif maxed_prob == probP:
            guess = "P"
        elif maxed_prob == probS:
            guess = "S"

        guessed.append(guess)
    return guess
