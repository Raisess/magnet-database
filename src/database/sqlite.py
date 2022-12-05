import sqlite3

class SqLite:
  def __init__(self, filename = "magnet_database.db"):
    self._conn = sqlite3.connect(filename, check_same_thread=False)

  def query(self, sql: str, parameters: list[any] = ()) -> list[any]:
    if sql.strip().startswith("INSERT"):
      try:
        cur = self._conn.cursor()
        cur.execute(sql, parameters)
        self._conn.commit()
      except Exception as exception:
        self._conn.rollback()
        raise exception
    else:
      cur = self._conn.cursor()
      cur.execute(sql, parameters)
      return cur.fetchall()
