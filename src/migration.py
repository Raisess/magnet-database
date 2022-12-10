#! /usr/bin/env python3

import os
from database.sqlite import SqLite

class Migrator:
  def __init__(self, path: str = "migrations"):
    self.__db = SqLite()
    self.__path = path

  def migrate(self) -> None:
    print("STARTED DATABASE MIGRATION PROCESS\n")

    for file in os.listdir(self.__path):
      if file.endswith(".sql"):
        with open(f"{self.__path}/{file}", "r") as opened_file:
          print(f"--> EXECUTING MIGRATION: {file}...")
          self.__db.query(opened_file.read())
          print(f"--> EXECUTED!")
      else:
        print("No .sql file detected in migrations folder")


if __name__ == "__main__":
  migrator = Migrator()
  migrator.migrate()
