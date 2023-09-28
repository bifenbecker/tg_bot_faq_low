from settings import settings

from .container import LawyerContainer

LawyerContainer.config.from_dict(settings.model_dump())
container = LawyerContainer()
container.wire(packages=[__name__])

__all__ = ("container", "LawyerContainer")
