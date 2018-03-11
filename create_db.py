import sqlite3

conn = sqlite3.connect("claims.db")
c = conn.cursor()

# create claim table
c.execute("""CREATE TABLE IF NOT EXISTS claims
            (date text, claim_num text, code text, provider text, amount real)""")

conn.commit()
conn.close()
