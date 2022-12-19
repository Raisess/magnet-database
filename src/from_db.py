#! /usr/bin/env python3

import os
from database.sqlite import SqLite
from repositories.magnet_link_repository import MagnetLinkRepository
from app.magnet_link.create_magnet_link import CreateMagnetLink

create_magnet_link = CreateMagnetLink(MagnetLinkRepository())

if __name__ == "__main__":
  user = os.getenv("USER")
  database = SqLite(f"/home/{user}/.magnet_database.db")
  magnets = database.query("SELECT alias, magnet_uri FROM magnets")

  for magnet in magnets:
    try:
      create_magnet_link.handle(magnet[0], magnet[1])
    except:
      pass
