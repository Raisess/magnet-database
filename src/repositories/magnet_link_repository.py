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
    data = self._db.query(f"SELECT * FROM magnet_links WHERE id = ?;", [id])
    return MagnetLinkModel(name=data[1], uri=data[2], creator_id=data[3], create_date=data[4], id=data[0], hash=data[5])

  def list_by_name(self, name: str) -> list[MagnetLinkModel]:
    data = self._db.query(f"SELECT * FROM magnet_links WHERE name LIKE '%{name}%';")

    result = []
    for item in data:
      result.append(MagnetLinkModel(name=item[1], uri=item[2], creator_id=item[3], create_date=item[4], id=item[0], hash=item[5]))

    return result
