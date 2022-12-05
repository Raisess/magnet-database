import uuid
import datetime

class MagnetLinkModel:
  create_date: str
  creator_id: str
  id: str
  name: str
  uri: str

  def __init__(
    self,
    name: str,
    uri: str,
    creator_id: str,
    create_date = datetime.datetime.utcnow().isoformat(),
    id = str(uuid.uuid4())
  ):
    self.name = name
    self.uri = uri
    self.creator_id = creator_id
    self.create_date = create_date
    self.id = id


CREATE_MAGNET_LINK_TABLE_QUERY = """
  CREATE TABLE magnet_links(
    id          VARCHAR(36),
    name        VARCHAR(100),
    uri         VARCHAR(255),
    creator_id  VARCHAR(36),
    create_date DATETIME
  );
"""
