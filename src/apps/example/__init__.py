from .container import ExampleContainer
from settings import settings

ExampleContainer.config.from_dict(settings.model_dump())
container = ExampleContainer()

container.wire(packages=[__name__])

__all__ = (
    container,
    ExampleContainer
)
