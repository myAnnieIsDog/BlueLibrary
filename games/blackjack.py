"""
Blackjack. The classic gambling card game.
Designed to be run from the gameroom module.
"""

# Standard Library
from pprint import pprint
import random
import time


# Main
def run():
    players = {
        "Player 1": {
            "ID": "999999999999",
            "Experience": 5,
            "Wager": 0,
            "Chips": 100,
            "Cards": [],
            "Score": 0,
            "Wins": 0,
            "Losses": 0,
            "Blackjacks": 0,
            "Busts": 0,
        }
    }
    blackjack(players)


def blackjack(players, decks=1):
    # PROD add select number of decks
    # The table class 'calling' this function should be passed as an argument.

    SUITS = str(chr(9829) + chr(9830) + chr(9824) + chr(9827))  #  ♥ ♦ ♠ ♣
    RANKS = "A23456789TJQK"
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append(rank + suit)
    DECK = tuple(deck)

    stack = []
    for i in range(decks):
        for card in DECK:
            stack.append(card)

    def loop(players):
        # Main game loop
        while True:
            # Shuffle
            random.shuffle(stack)

            # Deal to House
            house = {"Cards": [], "Score": 0}
            for _ in range(2):
                house["Cards"].append(stack.pop(0))

            # Deal to Players
            for player, data in players.items():
                data = {"Cards": [], "Score": 0}
                for _ in range(2):
                    data["Cards"].append(stack.pop(0))

            show_hands(house, players)

            for player, data in players.items():
                data = hitORstay(player, data)

            house = hit16stay17(house)

            show_hands(house, players, final=True)

            players = results(house, players)

            if not replay():
                break

    def score(cards):
        commons = 0  # SUM
        aces = 0  # COUNT
        tens = 0  # SUM
        for card in cards:
            rank = card[0:1]
            if rank.isdigit():
                commons = commons + int(rank)
            elif rank == "A":
                aces += 1
            else:
                tens += 10
        score = tens + commons + 11 * aces

        i = 0  # Aces reduce by 10 when score > 21
        while score > 21:
            if (aces - i) > 0:
                score -= 10 * i
                i += 1
            else:
                break
        return score

    def show_hands(house, players, final=False, width=16):
        # Iterate over player, cards
        for player, data in players.items():
            print((player + ": ").ljust(width), end="")
            for card in data["Cards"]:
                print("|" + card + "|", end="")
            points = score(data["Cards"])
            data["Score"] = points
            print(points)
        print()

        # Dealer shows one card or iterates over all
        a = "House: ".ljust(width)
        d = ""
        if final:
            for card in house["Cards"]:
                d = d + "|" + card + " |"
            print(a + d)
        else:
            b = "|" + house["Cards"][0] + " |"
            c = "|??|"
            print(a + b + c, end="  ")
        print()

    def hitORstay(player, data):
        while True:
            print(
                """
            {}, would you like to hit or stay?
                Hit, H, Yes, Y, or 1.
                Stay, S, No, N, 0, or <return>
            """.format(
                    player
                )
            )
            resp = input("").lower().strip()
            if resp in ["hit", "h", "yes", "y", "1"]:
                data["Cards"].append(stack.pop(0))
            else:
                print("{} stands.".format(player))
                return data

            points = score(data["Cards"])

            if points > 21:
                print("{} busted.".format(player))
                return data

            elif points == 21:
                print("!! {} has BLACKJACK !!".format(player))
                return data

    def hit16stay17(house):
        points = score(house["Cards"])
        while points < 17:
            time.sleep(1)
            house["Cards"].append(stack.pop(0))
            points = score(house["Cards"])
        return house

    def results(house, players):
        for player, data in players.items():
            points = data["Score"]
            if points == 21:
                data["Wins"] += 1
                data["Blackjack"] += 1
                print(player + " wins with Blackjack!")
            elif points > 21:
                data["Losses"] += 1
                data["Busts"] += 1
                print(player + " loses.")
            elif points == house["Score"]:
                data["Draws"] += 1
                print(player + " draws.")
            elif points >= house["Score"]:
                data["Wins"] += 1
                print(player + " wins!")
            elif points <= house["Score"]:
                data["Losses"] += 1
                print(player + " loses.")
            else:
                raise ValueError
        return players
        # print("Record: " + str(data))

    def replay():
        replay = input("\nPlay Again?\n").strip().lower()
        if replay in ["q", "quit", "x", "exit"]:
            return False
        return True

    loop(players)  # This calls the main game loop function that was defined at the top of blackjack()


if __name__ == "__main__":
    run()


