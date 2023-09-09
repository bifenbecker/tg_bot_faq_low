from abc import ABC, abstractmethod

from loguru import logger


class BaseStorage(ABC):
    def __init__(self):
        logger.info(f"Connect to storage - {self}")

    @abstractmethod
    def log(self, info):
        logger.info(info)
