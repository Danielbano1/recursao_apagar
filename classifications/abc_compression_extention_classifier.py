from abc import ABC, abstractmethod
from enum import Enum
from typing import Iterable

class CompressionExtension(Enum):
    SEVENZIP = '7z'
    ZIP = 'zip'
    TAR = 'tar'
    UNKNOWN = 'unknown'

class ABCCompressionExtensionClassifier(ABC):
    @abstractmethod
    def classify(self, path: str) -> CompressionExtension:
        pass

    @abstractmethod
    def classify_multiple(self, paths: Iterable[str]) -> dict[str, CompressionExtension]:
        pass
