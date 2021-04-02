from ._compat import Protocol
from typing import Any, List, TypeVar, Union


_T = TypeVar("_T")


class PackageMetadata(Protocol):
    def __len__(self) -> int:
        ...  # pragma: no cover

    def __contains__(self, item: str) -> bool:
        ...  # pragma: no cover

    def __getitem__(self, key: str) -> str:
        ...  # pragma: no cover

    def get_payload(self) -> str:
        ...  # pragma: no cover

    def get_all(self, name: str, failobj: _T = ...) -> Union[List[Any], _T]:
        """
        Return all values associated with a possibly multi-valued key.
        """
