from abc import ABCMeta, abstractmethod
from loguru import logger


class BaseStorage(metaclass=ABCMeta):
    def __init__(self):
        logger.info(f"Connect to storage - {self}")
