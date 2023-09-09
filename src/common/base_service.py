from abc import ABCMeta
from typing import Generic, TypeVar

RepoType = TypeVar("RepoType")


class BaseService(Generic[RepoType], metaclass=ABCMeta):
    def __init__(self, repo: RepoType):
        self._repo = repo

    @property
    def repo(self) -> RepoType:
        return self._repo
