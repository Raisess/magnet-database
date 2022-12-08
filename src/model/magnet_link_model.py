from datetime import datetime
from hashlib import sha256
from uuid import uuid4

class MagnetLinkModel:
  create_date: str
  creator_id: str
  id: str
  name: str
  uri: str
  hash: str

  def __init__(
    self,
    name: str,
    uri: str,
    creator_id: str,
    create_date: str = None,
    id: str = None,
    hash: str = None
  ):
    self.name = name
    self.uri = uri
    self.creator_id = creator_id
    self.create_date = create_date or datetime.utcnow().isoformat()
    self.id = id or str(uuid4())
    self.hash = hash or sha256((name + uri + creator_id + create_date + id).encode("utf-8")).hexdigest()


CREATE_MAGNET_LINK_TABLE_QUERY = """
  CREATE TABLE magnet_links(
    id          VARCHAR(36) UNIQUE,
    name        VARCHAR(100),
    uri         VARCHAR(255) UNIQUE,
    creator_id  VARCHAR(36),
    create_date DATETIME,
    hash        VARCHAR(64) UNIQUE
  );
"""
