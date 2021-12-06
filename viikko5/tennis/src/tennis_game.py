class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.love = {0: "Love-All",
                     1: "Fifteen-All",
                     2: "Thirty-All",
                     3: "Forty-All",
                     4: "Deuce"}

        self.adv_win = {0: "Deuce",
                        4: "Win for player1",
                        3: "Win for player1",
                        2: "Win for player1",
                        1: "Advantage player1",
                        -1: "Advantage player2",
                        -2: "Win for player2",
                        -3: "Win for player2",
                        -4: "Win for player2"}

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.m_score1 == self.m_score2:
            temp = self.m_score1
            score = self.love.get(temp, "X")
            return score
        if self.m_score1 >= 4 or self.m_score2 >= 4:
            temp = self.m_score1 - self. m_score2
            score = self.adv_win.get(temp, "X")
            return score
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

            return score
