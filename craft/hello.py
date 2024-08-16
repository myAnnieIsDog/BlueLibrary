from datetime import datetime as dt
from random import choice
from flask import Flask
from pprint import pprint



def main():
    start = startup()
    test_greetings()
    print(f"That took {dt.now() - start} seconds")



def startup():
    start = dt.now()
    print(start)
    return start


def test_greetings():
    hi = Greetings()
    hi.hello("World")
    hi.gripe()
    hi.goodbye()
    

class Greetings(object):
    def __init__(self) -> None:
        super().__init__()
                

    def hello(self, name):
        print(f"\nHello, {name}!")


    def gripe(self):
        sayings = (
            "MAY YOUR CHILDREN GROW TUSKS!",
            "Your converse is convoluted.",
            "I think not.",
            "FUCK OFF!",
            "L.A.M.E.",
            "Fuck around and find out.",
        )
        hmm = choice(sayings)
        print(f"{hmm}")


    def goodbye(self):
        parting_words = (
            "So long, and thanks for all the fish.",
            "Later, alligator.",
            "Bye!",
            "Adios.",
            "Hasta luego.",
        )
        bye = choice(parting_words)
        print(f"{bye}\n")


if __name__ == "__main__":
    main()