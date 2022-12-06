#! /usr/bin/env python3

from flask import Flask, request

from app.magnet_link.create_magnet_link import CreateMagnetLink
from app.magnet_link.search_magnet_links import SearchMagnetLinks
from controllers.magnet_link_controller import MagnetLinkController
from repositories.magnet_link_repository import MagnetLinkRepository
from view.view import View

app = Flask(__name__)

magnet_link_repository = MagnetLinkRepository()
magnet_link_controller = MagnetLinkController(
  CreateMagnetLink(magnet_link_repository),
  SearchMagnetLinks(magnet_link_repository)
)

@app.route("/", methods = ["GET"])
def index() -> str:
  html = View("index")
  return html.render()


@app.route("/create_magnet_link", methods = ["POST", "GET"])
def create_magnet_link() -> str:
  try:
    if request.method == "POST":
      magnet_link_controller.create_magnet_link()
      html = View("index")
      return html.render()
    else:
      # TODO: create create_magnet_link.html page
      html = View("magnet_link/create_magnet_link")
      return html.render()
  except Exception as exception:
    return "ERROR: " + str(exception)


@app.route("/search_magnet_links", methods = ["GET"])
def search_magnet_links() -> str:
  try:
    result = magnet_link_controller.search_magnet_links()
    html = View("magnet_link/search_magnet_links")
    return html.render({ "magnet_links": result })
  except Exception as exception:
    return "ERROR: " + str(exception)


if __name__ == "__main__":
  app.run()
