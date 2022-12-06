from flask import request

from app.magnet_link.create_magnet_link import CreateMagnetLink
from app.magnet_link.search_magnet_links import SearchMagnetLinks
from model.magnet_link_model import MagnetLinkModel

class MagnetLinkController:
  def __init__(
    self,
    create_magnet_link: CreateMagnetLink,
    search_magnet_links: SearchMagnetLinks
  ):
    self._create_magnet_link = create_magnet_link
    self._search_magnet_links = search_magnet_links

  def create_magnet_link(self) -> None:
    name = request.args.get("name")
    uri = request.args.get("uri")
    return self._create_magnet_link.handle(name, uri, "temp")

  def search_magnet_links(self) -> list[MagnetLinkModel]:
    name = request.args.get("name")
    return self._search_magnet_links.handle(name)
