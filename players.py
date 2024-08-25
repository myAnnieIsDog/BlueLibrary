"""
Player Profiles, Registration, Login, etc.
"""
# Standard Library
from dataclasses import dataclass
from datetime import datetime as dt
import hashlib
import hmac
import os
from perdict import PersistentDict as perdict
import sys
import time
from typing import Tuple

# Third Party
"""
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import sqlite3
from typing import List, Optional
"""


def run():  # Main
    p = Player()
    sys.exit(0)


"""
class db_Player(DeclarativeBase):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
"""


class Player:
    # Registration, Login, etc.
    def __init__(self):
        while True:
            action = input(
                """
            Enter: 
                r to register,
                l to login,
                g to play as a guest, or
                q to quit.
            """
            )
            if action == "r":
                self.register()
                break
            elif action == "l":
                self.login()
                break
            elif action == "g":
                self.guest()
                break
            elif action == "q":
                print("Thank you, come again.")
                sys.exit(0)
            # else: continue while True

    def register(self):
        with perdict("players.csv", "c", format="csv") as d:
            d["nxtID"] = 1
            self.ID = "id_{}".format(str(d["nxtID"]).zfill(12))
        self.name = input("\nWhat is your name?\n")
        self.email = input("\nWhat is your email?\n")
        self.active = []
        self.created = str()
        self.verified = False
        self.locked = False

        while True:
            pw1 = input("\nCreate your password.\n")
            pw2 = input("\nConfirm your password.\n")
            if pw1 != pw2:
                print("\nPasswords did not match. Try again.")
                continue
            self.password = pw1
            break

        salt = os.urandom(16)
        hash = hashlib.pbkdf2_hmac("sha256", pw1.encode(), salt, 100000)
        with perdict("players.csv", "c", format="csv") as d:
            d.update({self.email: (hash, salt)})

        print(
            """
            ID:        {}
            Name:      {}
            Email:     {}
            """.format(
                self.ID, self.name, self.email
            )
        )

        # PROD add send confim email

    def confirm(self, email):
        pass
        # PROD after clicking the confirmation email, verify the hash and update player.confirmed = True

    def login(self):
        while True:
            email = input("\nWhat is your email address?\n").strip().lower()
            pw1 = input("\nWhat is your password?\n").strip().lower()
            with open("players.csv", "rb") as f:
                print(dict(f.read())["email"])
                if hmac.compare_digest(
                    hash, hashlib.pbkdf2_hmac("sha256", pw1.encode(), salt, 100000)
                ):
                    self.active.append(dt.now())
                    print("Welcome to the party, pal.")
                    return True
            for i in range(5, 0, -1):
                print("Login failed. Try again in {} seconds.".format(i + 1))
                time.sleep(1)

    def guest(self):
        with perdict("players.csv", "c", format="csv") as d:
            d["guest"] += 1
            self.ID = "guest_{}".format(str(d["guest"]).zfill(18))
        self.name = input("\nWhat is your name?\n")
        print(
            """
            ID:        {}
            Name:      {}
            """.format(
                self.ID, self.name
            )
        )


if __name__ == "__main__":
    run()

