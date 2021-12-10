import unittest
from bowling import roll_the_ball, calculate_score
import pandas as pd

class TestBowling(unittest.TestCase):

    def test_roll_the_ball(self):
        result = roll_the_ball(1)
        # The first bowl in a round is not more than 10.
        self.assertLessEqual(result["first_bowl"].item(), 10)
        # The sum of the first and second bowls in a round do not equal more than 10
        self.assertLessEqual(result["first_bowl"].item() + result["second_bowl"].item(), 10)

    def test_calculate_score(self):
        input_data = pd.DataFrame([[1, 7, 3, "Spare", 10],[2, 7, 2, "", 0]],
                                    columns=["bowling_round", "first_bowl", "second_bowl", "spare_or_strike", "round_score"])
        output_data = calculate_score(input_data, 2)
        # The round 1 score should be 17 (given the input data).
        self.assertEqual(output_data.loc[output_data['bowling_round'] == 1, "round_score"].item(), 17)
        # The round score cannot be less than 0.
        self.assertGreater(output_data.loc[output_data['bowling_round'] == 2, "round_score"].item(), -1)

if __name__ == "__main__":
    unittest.main()