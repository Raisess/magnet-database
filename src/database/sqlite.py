import sqlite3

class SqLite:
  def __init__(self, filename = "magnet_database.db"):
    self.__conn = sqlite3.connect(filename, check_same_thread=False)

  def query(self, sql: str, parameters: list[any] = ()) -> list[any]:
    if sql.strip().startswith("INSERT"):
      try:
        cur = self.__conn.cursor()
        cur.execute(sql, parameters)
        self.__conn.commit()
      except Exception as exception:
        self.__conn.rollback()
        raise exception
    else:
      cur = self.__conn.cursor()
      cur.execute(sql, parameters)
      return cur.fetchall()
