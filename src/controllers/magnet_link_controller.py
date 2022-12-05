from flask import request
from app.magnet_link.create_magnet_link import CreateMagnetLink

class MagnetLinkController:
  def __init__(self, create_magnet_link: CreateMagnetLink):
    self._create_magnet_link = create_magnet_link

  def create_magnet_link(self):
    name = request.args.get("name")
    uri = request.args.get("uri")

    self._create_magnet_link.handle(name, uri, "temp")
