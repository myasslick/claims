import csv
import sqlite3

def select_claims(conn):
    c = conn.cursor()
    c.execute("""SELECT DISTINCT date, claim_num, code, provider, amount
                 FROM claims ORDER BY date ASC, code ASC;""")
    results = c.fetchall()
    return results

def export_to_csv(results):
    field_names = ["date", "claim_num", "code", "provider", "amount"]
    with open("claims.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        for r in results:
            date, claim_num, code, provider, amount = r
            if provider == "GAR":
                provider = "GARCIASOSA"
            writer.writerow({
                "date": date, "claim_num": claim_num,
                "code": code, "provider": provider,
                "amount": amount
            })

def main():
    conn = sqlite3.connect("claims.db")
    results = select_claims(conn)
    export_to_csv(results)
    print("{count} claim records are written to claims.csv".format(
        count=len(results)))

if __name__ == "__main__":
    main()
