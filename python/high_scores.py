"""My task is to write methods that return the highest score from the list,
the last added score and the three highest scores. """
# Input: scores = [30, 50, 20, 70]
# Output: expected = [30, 50, 20, 70]
# Processing:
# Class that gives a report of high scores
class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def list_of_scores(self):
        return self.scores

    def latest(self):
        """Return the last added score."""
        last_element_index = len(self.scores) - 1 # get the last index
        return self.scores[last_element_index] # return the last element

    def personal_best(self):
        """Return highest score in a list"""
        max = self.scores[0] # initially set max to first score value
        # loop through scores and find the max score
        for current_score in self.scores:
            if current_score > max:
                max = current_score
        return max

    def personal_top_three(self):
        """Return the three highest scores in a list"""
        # Before we return the top 3 scores lets make sure given at least 3 scores
        if len(self.scores) >= 3:
            copy_scores = self.scores
            found = 0 # Initialize a flag for when we have found 3 scores
            max_score_pos = 0 # keep track of the position of the max score
            top_3 = [] # store the result
            # Loop through the scores and find the top three
            while found != 3: # when we have 3 top scores stop
                max_score_pos = copy_scores.index(max(copy_scores))
                max_score_value = copy_scores.pop(max_score_pos)
                top_3.append(max_score_value)
                found += 1
            return top_3
        else: # if there are less than three scores then return the scores from
        # greatest to least
            self.scores.sort(reverse=True)
            return self.scores

# highScore = HighScores([30, 70])
# print(highScore.personal_top_three())
