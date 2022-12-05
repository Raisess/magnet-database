#! /usr/bin/env python3

from database.sqlite import SqLite
from model.magnet_link_model import CREATE_MAGNET_LINK_TABLE_QUERY
from repositories.magnet_link_repository import MagnetLinkRepository

if __name__ == "__main__":
  db = SqLite()
  db.query(CREATE_MAGNET_LINK_TABLE_QUERY)
