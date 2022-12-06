from app.magnet_link.create_magnet_link import CreateMagnetLink
from app.magnet_link.search_magnet_links import SearchMagnetLinks
from controllers.magnet_link_controller import MagnetLinkController
from repositories.magnet_link_repository import MagnetLinkRepository

magnet_link_repository = MagnetLinkRepository()
magnet_link_controller = MagnetLinkController(
  CreateMagnetLink(magnet_link_repository),
  SearchMagnetLinks(magnet_link_repository)
)
