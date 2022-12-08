from app.magnet_link.create_magnet_link import CreateMagnetLink
from app.magnet_link.search_magnet_links import SearchMagnetLinks
from model.magnet_link_model import MagnetLinkModel

class MagnetLinkController:
  def __init__(
    self,
    create_magnet_link: CreateMagnetLink,
    search_magnet_links: SearchMagnetLinks
  ):
    self.__create_magnet_link = create_magnet_link
    self.__search_magnet_links = search_magnet_links

  def create_magnet_link(self, name: str, uri: str) -> None:
    if not uri.startswith("magnet:?") and not uri.endswith(".torrent"):
      raise Exception("Invalid uri format, try a .torrent file or a magnet link")

    return self.__create_magnet_link.handle(name, uri, "temp")

  def search_magnet_links(self, name: str) -> list[MagnetLinkModel]:
    return self.__search_magnet_links.handle(name)
