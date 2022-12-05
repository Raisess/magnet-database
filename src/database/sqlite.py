import sqlite3

class SqLite:
  def __init__(self, filename = "magnet_database.db"):
    self._db = sqlite3.connect(filename)

  def query(self, sql: str, parameters: list[any] = ()) -> list[any]:
    res = self._db.cursor()
    res.execute(sql.strip(), parameters)
    if sql.strip().startswith("INSERT"):
      self._db.commit()
    else:
      return res.fetchall()
