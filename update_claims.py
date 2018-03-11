#!/usr/bin/env python3
import sqlite3

def update_claim(conn):
    c = conn.cursor()

    claim_num = input("enter claim number to be changed: ")
    date = input("enter claim date: ")
    old_provider = input("enter old provider name: ")
    new_provider = input("enter new provider name: ")
    data = (new_provider, claim_numer, date, old_provider)

    c.execute("""UPDATE claims SET provider = (?)
        WHERE claim_numer = (?) AND date = (?) AND provider = (?);""", data)
    conn.commit()

def main():
    print("Poor man's claim data entry system is initiated. Follows \
instructions please.")

    conn = sqlite3.connect("claims.db")
    c = conn.cursor()

    count = 0
    while True:
        print("")
        update_clain(conn)
        count += 1
        do_continue = input("Continue? ('q' exit): ")
        if do_continue.lower() == "q":
            conn.close()
            break
    print("Total of {count} claims updated.".format(count=count))

if __name__ == "__main__":
    main()
