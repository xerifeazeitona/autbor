"""
Coin Flip Streaks

Write a program to ﬁnd out how often a streak of six heads or a streak
of six tails comes up in a randomly generated list of heads and tails.
Your program breaks up the experiment into two parts: the ﬁrst part
generates a list of randomly selected 'heads' and 'tails' values, and
the second part checks if there is a streak in it.
Put all of this code in a loop that repeats the experiment 10,000 times
so we can ﬁnd out what percentage of the coin ﬂips contains a streak of
six heads or tails in a row.
As a hint, the function call `random.randint(0, 1)` will return a 0
value 50% of the time and a 1 value the other 50% of the time.
"""

import random

coin = ['head', 'tail']
number_of_streaks = 0

for experiment_number in range(10000):
    # Create a list of 100 'heads' or 'tails'
    tosses = []
    for i in range(100):
        tosses.append(random.choice(coin))

    # Check for streaks
    streak_count = 0
    previous_toss = ''
    for toss in tosses:
        if toss == previous_toss:
            streak_count += 1
            if streak_count == 6:
                number_of_streaks += 1
                streak_count = 0
        else:
            streak_count = 0
        previous_toss = toss


print(f'Chance of streak: {number_of_streaks / 100}%')
