"""
This is for keeping score playing pickleball
"""
import datetime
import time


PI5 = 3.14159
STANDARD_MATCH = 'of=3, to=11, by=2, timeouts=1'


def run():
    match1 = Match(STANDARD_MATCH)


class Match(of=3, to=11, by=2, timeouts=1):
    def __init__(self):
        self.of = of
        self.to = to
        self.by = by
        self.home_games = 0
        self.visitor_games = 0
        self.home_tomeouts = timeouts
        self.visitor_timeouts = timeouts
        self.home_opening_position = True
        self.visitor_opening_position = True
        self.home = 0
        self.visitor = 0
        self.home_serving = True
        self.server = 2
        self.receiver = 1
        self.score_now = "0-0-2"
        self.score_log = ["0-0-2 Opening Serve"]

    def side(self):
        # A service side:
        # returns 0 on Sideout
        # returns 1 on Wins Game
        # returns 2 on Wins Match
        # otherwise continues loop

        while True:
            # The result of this serve
            result = input("h Home, v Visitor, or r Replay:")

            # Replay (for hinderance, uncertain result, etc.)
            if result.lower().strip('').replace(' ', '') in ("r", "replay":
                self.score_log.append(self.score_now + "Replay")

            # Serving team faults / Returning team wins
            elif (result == "v" and self.home_serving) or (
                result == "h" and not self.home_serving
            ):
                if self.serving == 2:
                    self.home_serving = not self.home_serving
                    self.score_log.append(self.score_now + "Sideout")
                    return 0

                if self.serving == 1:
                    self.server = 2
                    self.score_log.append(self.score_now + "Second Server")

            # Returning team faults / Serving team wins
            elif result == "v" or result == "h":
                # Home is serving
                if result == "h" and self.home_serving:
                    self.home += 1
                    if self.wins_game(self.home, self.visitor, serving):
                        if self.wins_match(self.home_games, serving):
                            return 2
                        else:
                            return 1

                # Visitor is servimg
                if result == "v" and not self.home_serving:
                    self.visitor += 1
                    if self.wins_game(self.visitor, self.home, serving):
                        if self.wins_match(self.visitor_games, serving):
                            return 2
                        else:
                            return 1

                self.score_now = "{}-{}-{}".format(self.home, self.visitor, self.server)
                self.score_log.append(self.score_now + "Point")

        def wins_game(self, a, b, serving):
            if (a >= self.to) and (a - b >= self.by):
                self.score_log.append("{} Wins the game!".format(serving))
                return True
            else:
                return False

        def wins_match(self, games, serving):
            if games >= (self.of // 2 + 1):
                self.score_log.append("{} Wins the match!".format(serving))
                return True
            else:
                return False
                
   s = self.side()


if __name__ == "__main__":
    run()

