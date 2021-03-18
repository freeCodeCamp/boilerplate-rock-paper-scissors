# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random


def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    guess = "R"
    if len(opponent_history) >= 3:
        df = {}
        for i in range(2, len(opponent_history)):
            key = "".join([str(x) for x in opponent_history[i - 2 : i]])
            if key not in df:
                df[key] = [opponent_history[i]]
            else:
                df[key].append(opponent_history[i])

    last_key = opponent_history[-2:]
    if last_key in opponent_history:
        probR = 100 * (df[last_key].count("R") / len(df[last_key]))
        probP = 100 * (df[last_key].count("P") / len(df[last_key]))
        probS = 100 * (df[last_key].count("S") / len(df[last_key]))

        max_probability = max(probR, probP)
        max_probability = max(max_probability, probS)
        if max_probability == probR:
            guess = "P"
        elif max_probability == probP:
            guess = "S"
        elif max_probability == probS:
            guess = "R"

    return guess
