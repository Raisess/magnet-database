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
    create_date: str = None,
    id: str = None,
    hash: str = None
  ):
    self.name = name
    self.uri = uri
    self.create_date = create_date or datetime.utcnow().isoformat()
    self.id = id or str(uuid4())
    self.hash = hash or sha256(
      (self.name + self.uri + self.create_date + self.id).encode("utf-8")
    ).hexdigest()
