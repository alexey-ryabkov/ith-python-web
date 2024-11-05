import mysql.connector
from .utils import execute_sql_file
from ..config import DB_CONFIG


class DatabaseManager:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)
        self.prepare()

    def prepare(self):
        print("prepare!!!")
        self._create_tables()
        self.cursor.execute("SELECT COUNT(*) as cnt FROM Event")
        if self.cursor.fetchone()["cnt"] == 0:
            self._load_init_data()

        self.conn.commit()

    def _create_tables(self):
        execute_sql_file(self.cursor, "./app/db/create_tables.sql")

    def _load_init_data(self):
        # SELECT * FROM Team;
        # -- TRUNCATE TABLE Event; TRUNCATE TABLE Team; TRUNCATE TABLE Tournament;
        execute_sql_file(self.cursor, "./app/db/fill_dummy_data.sql")

    def __enter__(self):
        # self.cursor = self.conn.cursor(dictionary=True)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
