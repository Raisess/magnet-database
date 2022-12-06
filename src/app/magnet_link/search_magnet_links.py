from model.magnet_link_model import MagnetLinkModel
from repositories.magnet_link_repository import MagnetLinkRepository

class SearchMagnetLinks:
  def __init__(self, magnet_link_repository: MagnetLinkRepository):
    self._magnet_link_repository = magnet_link_repository

  def handle(self, name: str) -> list[MagnetLinkModel]:
    return self._magnet_link_repository.list_by_name(name)
