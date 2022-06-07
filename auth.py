def authenticate(conn, username, password):
    query = f"SELECT Password FROM Authentication WHERE Username='{username}';"
    cursor = conn.cursor()
    cursor.execute(query)
    authpass = "null"
    for row in cursor:
        authpass = row[0]
    return authpass == password