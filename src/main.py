#! /usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# magnet link related
from app.magnet_link.create_magnet_link import CreateMagnetLink
from app.magnet_link.search_magnet_links import SearchMagnetLinks
from controllers.magnet_link_controller import MagnetLinkController
from repositories.magnet_link_repository import MagnetLinkRepository

magnet_link_repository = MagnetLinkRepository()
magnet_link_controller = MagnetLinkController(
  CreateMagnetLink(magnet_link_repository),
  SearchMagnetLinks(magnet_link_repository)
)

@app.route("/create_magnet_link", methods = ["POST"])
def create_magnet_link() -> str:
  try:
    magnet_link_controller.create_magnet_link()
    return "OK"
  except Exception as exception:
    return "ERROR: " + str(exception)

@app.route("/search_magnet_links", methods = ["GET"])
def search_magnet_links() -> str:
  try:
    result = magnet_link_controller.search_magnet_links()
    response = ""

    for item in result:
      response += item.id + ": " + item.name + "\n"

    return response
  except Exception as exception:
    return "ERROR: " + str(exception)


if __name__ == "__main__":
  app.run()
