import sqlite3

class Connection:
    def __init__(self, db: str):
        self._db_connection = sqlite3.connect(db)
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        return self._db_cur.execute(query, params)

    def getLastRowId(self):
        return self._db_cur.lastrowid

    def commit(self) -> None:
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()