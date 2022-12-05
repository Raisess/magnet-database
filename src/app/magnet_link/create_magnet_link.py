from model.magnet_link_model import MagnetLinkModel
from repositories.magnet_link_repository import MagnetLinkRepository

class CreateMagnetLink:
  def __init__(self, magnet_link_repository: MagnetLinkRepository):
    self._magnet_link_repository = magnet_link_repository

  def handle(self, name: str, uri: str, creator_id: str) -> None:
    self._magnet_link_repository.create(MagnetLinkModel(name, uri, creator_id))
