import sqlite3

class SqLite:
  def __init__(self, filename = "magnet_database.db"):
    self.__conn = sqlite3.connect(filename, check_same_thread=False)

  def query(self, sql: str, parameters: list[any] = ()) -> list[any]:
    try:
      cursor = self.__conn.cursor()
      cursor.execute(sql, parameters)
      self.__conn.commit()
      return cursor.fetchall()
    except Exception as exception:
      self.__conn.rollback()
      raise exception
