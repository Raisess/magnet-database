from database.sqlite import SqLite

class Repository:
  def __init__(self):
    self._db = SqLite()
