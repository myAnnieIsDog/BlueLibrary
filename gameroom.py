"""
A place to play games. 
First goal: Blackjack.
"""
# Standard Library
import random
import sqlite3
import time
from typing import List, Optional

# Project modules
from blackjack import blackjack
from players import Player



def run():
    # PROD support tables > 1
    
    table = Table()
    player = Player()
    table.select_game(player)


class Table(object):
    GAMES = {
        'Blackjack': blackjack(),
    }
    LOCATIONS = (  # not used. Base of the long-term plan to create a story arc.
        "The Dumpster",
        "The Garage",
        "The Casino",
        "The Living Room",
        "The High Rollers Room",
        "The Penthouse",
        "The World Series",
        "The Secret Location",
    )
        
    def select_game():
        print('Available Games: ')
        for i in GAMES.keys():
            print(i)
            
        g = input()'Select Game:').strip().lower()
        if g in ['b', 'bj', 'blackjack']:
            table1.players = blackjack(table1.players)

'''
class db_Counters(DeclarativeBase):
    __tablename__ = "counters"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    next: Mapped[Optional[str]]


class db_Table(DeclarativeBase):
    __tablename__ = "card_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
'''

if __name__ == "__main__":
    run()

