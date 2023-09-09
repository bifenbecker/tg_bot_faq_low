from settings import settings

from .container import ExampleContainer

ExampleContainer.config.from_dict(settings.model_dump())
container = ExampleContainer()

container.wire(packages=[__name__])

__all__ = ("container", "ExampleContainer")
