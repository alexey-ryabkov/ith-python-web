def get_events_data(cursor, fav_4user=None, filter_fav=False):
    filter_fav = fav_4user and filter_fav
    SQL = f"""
        SELECT 
          e.id, 
          e.time_start, 
          t.name AS tournament, 
          ht.name AS home_team, 
          CONCAT(home_team_score, ':', guest_team_score) AS score, 
          gt.name AS guest_team {
            """, CASE
              WHEN fe.user IS NOT NULL THEN TRUE 
              ELSE FALSE 
            END AS is_favorite""" 
          if fav_4user 
          else ""}
        FROM Event e 
        JOIN Tournament t ON e.tournament = t.id 
        JOIN Team ht ON e.home_team = ht.id 
        JOIN Team gt ON e.guest_team = gt.id
        """
    if filter_fav:
        SQL += """
            JOIN FavoriteEvent fe ON e.id = fe.event 
            WHERE fe.user = %s
        """
        cursor.execute(SQL, (fav_4user,))
    else:
        if fav_4user:
            SQL += "LEFT JOIN FavoriteEvent fe ON e.id = fe.event AND fe.user = %s"
            cursor.execute(SQL, (fav_4user,))
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


def del_event_from_fav(cursor, event_id, user_id):
    cursor.execute(
        "SELECT 1 FROM FavoriteEvent WHERE user = %s AND event = %s",
        (user_id, event_id),
    )
    if cursor.fetchone():
        cursor.execute(
            "DELETE FROM FavoriteEvent WHERE user = %s AND event = %s",
            (user_id, event_id),
        )
        return True
    else:
        return False
