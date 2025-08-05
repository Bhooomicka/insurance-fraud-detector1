import sqlite3

# Connect to the SQLite DB
conn = sqlite3.connect("insurance.db")
cursor = conn.cursor()

# Read SQL file
with open("sql_fraud_queries.sql", "r") as file:
    sql_script = file.read()

# Split into individual queries (by semicolon)
queries = [q.strip() for q in sql_script.split(";") if q.strip()]

# Run and print each query result
for i, query in enumerate(queries, 1):
    print(f"\n--- Running Query {i} ---")
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        print(columns)
        for row in results:
            print(row)
    except Exception as e:
        print(f"Error running query {i}: {e}")

conn.close()
