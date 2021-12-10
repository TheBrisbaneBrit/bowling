from bowling import roll_the_ball, calculate_score
import pandas as pd

bowling_results = pd.DataFrame(columns=["bowling_round", "first_bowl", "second_bowl", "spare_or_strike", "round_score"])

#This loop simulates a session of bowling
for bowling_round in list(range(1,11)):

    this_round_results = roll_the_ball(bowling_round)
    bowling_results = bowling_results.append(this_round_results)
    bowling_results = calculate_score(bowling_results, bowling_round)

#Sum up all of the scores from each round to produce the total round score.
total_score = bowling_results["round_score"].sum()

print(bowling_results.to_string(index=False))
print("The total score was {}".format(total_score))