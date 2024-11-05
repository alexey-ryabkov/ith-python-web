def get_events_data(cursor, fav4_user_id=None):
    SQL = """
        SELECT 
          e.id, 
          e.time_start, 
          t.name AS tournament, 
          ht.name AS home_team, 
          CONCAT(home_team_score, ':', guest_team_score) AS score, 
          gt.name AS guest_team  
        FROM Event e 
        JOIN Tournament t ON e.tournament = t.id 
        JOIN Team ht ON e.home_team = ht.id 
        JOIN Team gt ON e.guest_team = gt.id
        """
    if fav4_user_id:
        SQL += """
            JOIN FavoriteEvent fe ON e.id = fe.event 
            WHERE fe.user = %s
        """
        cursor.execute(SQL, (fav4_user_id,))
    else:
        cursor.execute(SQL)
    return cursor.fetchall()


def add_event_2fav(cursor, event_id, user_id):
    cursor.execute(
        "SELECT 1 FROM FavoriteEvent WHERE user = %s AND event = %s",
        (user_id, event_id),
    )
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO FavoriteEvent (user, event) VALUES (%s, %s)",
            (user_id, event_id),
        )
        return True
    else:
        return False
