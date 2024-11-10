def is_unique_login_email(cursor, login, email):
    cursor.execute(
        "SELECT COUNT(*) as cnt FROM User WHERE login = %s OR email = %s",
        (login, email),
    )
    return cursor.fetchone()["cnt"] == 0


def create_user(cursor, login, email, password):
    cursor.execute(
        "INSERT INTO User (login, email, password) VALUES (%s, %s, %s)",
        (login, email, password),
    )


def edit_user(cursor, user_id, login, email, password):
    cursor.execute(
        """
        UPDATE User 
        SET login = %s, email = %s, password = %s 
        WHERE id = %s
        """,
        (login, email, password, user_id),
    )


def get_user_data(cursor, identifier):
    SQL = "SELECT * FROM User WHERE "
    if isinstance(identifier, str):
        SQL += "login = %s"
    elif isinstance(identifier, int):
        SQL += "id = %s"
    else:
        return None
    cursor.execute(SQL, (identifier,))
    return cursor.fetchone()
