import sqlite3


def run():
    add_counters()
    verify()
    

def verify():
    for row in cur.execute("SELECT name FROM sqlite_master"):
        print(row)

    for row in cur.execute("SELECT * FROM player"):
        print(row)
        
    for row in cur.execute("SELECT * FROM counters"):
        print(row)
    
def create_tables():
    cur.execute("CREATE TABLE IF not exists counters(id, category, count)")
    cur.execute("CREATE TABLE player(id, name, email, active, created, verified, locked)")

def add_counters():
    cur.execute("INSERT INTO counters VALUES (user, 1)")
    cur.execute("INSERT INTO counters VALUES (guest, 1)")
    con.commit()
    
    
def add_players():
    data = [
        (
            1,
            "Scott",
            "scottdoolittle@gmail.com",
            "true",
            "12/22/1981",
            "5/13/2017",
            "false",
        ),
        (2, "Erin", "eakelly82@gmail.com", "true", "10/08/1982", "5/13/2017", "false"),
    ]
    
    cur.execute("INSERT INTO player VALUES(?)", data)
    con.commit()


if __name__ == "__main__":
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    run()
    con.close

