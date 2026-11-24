import psycopg

# Connection string format: postgresql://user:password@host:port/dbname
CONN_INFO = "postgresql://postgres:your_password@localhost:5432/myapp"

def main():
    # Connect to the database
    with psycopg.connect(CONN_INFO) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM members;")
            for record in cur.fetchall():
                print(record)

            conn.commit()

if __name__ == "__main__":
    main()
