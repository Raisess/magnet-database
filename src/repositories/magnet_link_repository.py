from model.magnet_link_model import MagnetLinkModel
from repositories.repository import Repository

class MagnetLinkRepository(Repository):
  def __init__(self):
    super().__init__()

  def create(self, data: MagnetLinkModel) -> None:
    self._db.query(
      f"INSERT INTO magnet_links(id, name, uri, create_date, hash) VALUES(?, ?, ?, ?, ?);",
      [data.id, data.name, data.uri, data.create_date, data.hash]
    )

  def get(self, id: str) -> MagnetLinkModel:
    data = self._db.query(f"SELECT * FROM magnet_links WHERE id = ?;", [id])
    return MagnetLinkModel(name=data[1], uri=data[2], create_date=data[3], id=data[0], hash=data[4])

  def list_by_name(self, name: str) -> list[MagnetLinkModel]:
    data = self._db.query(f"SELECT * FROM magnet_links WHERE name LIKE '%{name}%';")
    return [
      MagnetLinkModel(name=item[1], uri=item[2], create_date=item[3], id=item[0], hash=item[4])
      for item in data
    ]
