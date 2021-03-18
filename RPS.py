# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

guessed = []
counter = 0


def player(prev_play, opponent_history=[]):
    global guessed
    global counter
    if len(guessed) > 0 and len(guessed) % 1000 == 0:
        counter += 1

    third = 1 / 3
    opponent_history.append(prev_play)

    markov_df = {}
    # OUR NEXT MOVE      R   ,   P  ,   S
    markov_df["PR"] = [third, third, third]
    markov_df["PP"] = [third, third, third]
    markov_df["PS"] = [third, third, third]
    markov_df["RR"] = [third, third, third]
    markov_df["RP"] = [third, third, third]
    markov_df["RS"] = [third, third, third]
    markov_df["SR"] = [third, third, third]
    markov_df["SP"] = [third, third, third]
    markov_df["SS"] = [third, third, third]

    new_guessed = guessed[counter * 1000 :]
    new_opponent = opponent_history[counter * 1000 :]

    if len(new_guessed) <= 3:
        guess = random.choice(["R", "P", "S"])
        guessed.append(guess)
    elif len(new_guessed) > 3:
        for i in range(len(new_guessed) - 1):
            key = new_guessed[i] + new_opponent[i]
            if len(key) < 2:
                key = new_guessed[i] * 2
            next_move = new_opponent[i + 1]
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

        last_key = new_guessed[-1] + new_opponent[-1]
        if len(last_key) < 2:
            last_key = new_guessed[-1] * 2
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
