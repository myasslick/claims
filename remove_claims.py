import sqlite3

def remove_claim(conn):
    claim_num = input("enter claim number to delete: ")
    code = input("enter code to delete: ")
    c = conn.cursor()
    c.execute("DELETE FROM claims where claim_num = (?) AND code = (?);",
        (claim_num, code))
    conn.commit()

def main():
    conn = sqlite3.connect("claims.db")
    count = 0
    while True:
        remove_claim(conn)
        count += 1
        do_continue = input("Continue? ('q' to exit): ")
        if do_continue.lower() == 'q':
            conn.close()
            break

    print("Total of {count} records deleted.".format(count=count))

if __name__ == "__main__":
    main()
