from model.magnet_link_model import MagnetLinkModel
from repositories.repository import Repository

class MagnetLinkRepository(Repository):
  def __init__(self):
    super().__init__()

  def create(self, data: MagnetLinkModel) -> None:
    self._db.query(
      f"INSERT INTO magnet_links(id, name, uri, creator_id, create_date, hash) VALUES(?, ?, ?, ?, ?, ?);",
      [data.id, data.name, data.uri, data.creator_id, data.create_date, data.hash]
    )

  def get(self, id: str) -> MagnetLinkModel:
    return self._db.query(f"SELECT * FROM magnet_links WHERE id = ?;", [id])

  def list_by_name(self, name: str) -> list[MagnetLinkModel]:
    return self._db.query(f"SELECT * FROM magnet_links WHERE name = ?;", [name])
