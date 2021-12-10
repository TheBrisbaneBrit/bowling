import pandas as pd
import random

## Using pandas as a lightweight database. A better solution would be to use a SQL database.

def roll_the_ball(bowling_round):
    """
    The function generates random numbers for both the first and second bowls and determines whether the player scored a spare or a strike.
    The first bowl is a random number between 0 and 10. The second bowl is a random number between 0 and the number of remaining pins.
    Args:
        bowling_round (int): An integer between 1 and 10 which represents the round of bowling in a session.
    Returns:
        A pandas Dataframe with that contains the bowling round, first bowl in the round, second bowl in the round, whether the player
        scored a Strike/Spare or not and a score for the round.
    """
    assert 1 <= bowling_round <= 10, "Bowling round must be between 1 and 10."
    first_bowl = random.randint(0,10)
    second_bowl = random.randint(0,10 - first_bowl)
    if first_bowl == 10:
        spare_or_strike = "Strike"
    elif first_bowl + second_bowl == 10:
        spare_or_strike = "Spare"
    else:
        spare_or_strike = ""
    results_this_round = pd.DataFrame([[bowling_round, first_bowl, second_bowl, spare_or_strike, first_bowl + second_bowl]],
                                        columns=["bowling_round", "first_bowl", "second_bowl", "spare_or_strike", "round_score"])
    return results_this_round

def calculate_score(bowling_results, bowling_round):
    """
    The function looks at whether the previous bowling round was a spare or strike and then calculates the appropriate score for the last round.
    If in 2 tries, the bowler knocks down all the pins, it is a spare. The scoring of a spare is the sum of the number of pins knocked down plus 
    the number of pins knocked down in the next bowl.
    If in one try, the bowler knocks down all the pins, it is a strike. The scoring of a strike is the sum of the number of pins knocked down plus 
    the number of pins knocked down in the next two bowls.
    Args:
        bowling_results(pandas.DataFrame): A pandas dataframe that contains the results from a round of bowling. The DataFrame should contain the 
        bowling round, first bowl in the round, second bowl in the round, whether the player scored a Strike/Spare or not and a dummy value of 0 for 
        the round score.
        bowling_round (int): An integer between 1 and 10 which represents the round of bowling in a session.
    Returns:
        A pandas dataframe with the historical bowling results and an updated score for a given round.
    """
    previous_round_spare_or_strike = bowling_results.loc[bowling_results['bowling_round'] == bowling_round -1, "spare_or_strike"].to_string(index=False)
    first_bowl = bowling_results.loc[bowling_results['bowling_round'] == bowling_round, "first_bowl"].item()
    second_bowl = bowling_results.loc[bowling_results['bowling_round'] == bowling_round, "second_bowl"].item()
    current_round_score = first_bowl + second_bowl
    if bowling_round == 1:
        previous_round_score = 0
    elif 2 <= bowling_round <= 10:
        if previous_round_spare_or_strike == "":
            previous_round_score = bowling_results.loc[bowling_results['bowling_round'] == bowling_round -1, "round_score"]
        elif previous_round_spare_or_strike == "Spare":
            previous_round_score = 10 + first_bowl
        elif previous_round_spare_or_strike == "Strike":
            previous_round_score = 10 + first_bowl + second_bowl
    updated_bowling_results = bowling_results.copy()
    updated_bowling_results.loc[updated_bowling_results['bowling_round'] == bowling_round, "round_score"] = current_round_score
    updated_bowling_results.loc[updated_bowling_results['bowling_round'] == bowling_round - 1, "round_score"] = previous_round_score
    return updated_bowling_results


