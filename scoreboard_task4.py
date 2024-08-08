

class Scoreboard:
    def __init__(self):
        self.user_score=0
        self.computer_score=0
        self.update_score()
    def you_win(self):
        self.user_score+=1
        self.update_score()
    def you_loose(self):
        self.computer_score+=1
        self.update_score()

    def update_score(self):
        print(f"YOUR SCORE:{self.user_score}      COMPUTER SCORE:{self.computer_score}")
    def reset(self):
        self.user_score = 0
        self.computer_score = 0


