import os
import mysql.connector
from .utils import execute_sql_file
from ..config import APP_CONFIG


def _get_path(sql):
    return os.path.join(os.path.dirname(__file__), sql)


class DatabaseManager:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(**APP_CONFIG["db"])
            self.cursor = self.conn.cursor(dictionary=True)
            self.prepare()
        except mysql.connector.Error as e:
            if e.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                # `ll try to create db if it appears to be unknown
                db_config_wo_database = {
                    k: v for k, v in APP_CONFIG["db"].items() if k != "database"
                }
                self.conn = mysql.connector.connect(**db_config_wo_database)

                cursor = self.conn.cursor(dictionary=True)
                cursor.execute(f"CREATE DATABASE {APP_CONFIG['db']['database']}")
                self.conn.commit()
                cursor.execute(f"USE {APP_CONFIG['db']['database']}")
                cursor.close()

                self.cursor = self.conn.cursor(dictionary=True)
                self.prepare()
            else:
                raise e

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def prepare(self):
        # print("prepare!!!")
        self._create_tables()
        self.cursor.execute("SELECT COUNT(*) as cnt FROM Event")
        if self.cursor.fetchone()["cnt"] == 0:
            self._load_init_data()
        self.conn.commit()

    def _create_tables(self):
        execute_sql_file(self.cursor, _get_path("create_tables.sql"))

    def _load_init_data(self):
        execute_sql_file(self.cursor, _get_path("fill_dummy_data.sql"))
