from abc import ABC, abstractmethod
import io

from classifications.abc_compression_extention_classifier import ABCCompressionExtensionClassifier, CompressionExtension

class ABCCompressedDocuments(ABC):
    @abstractmethod
    def extract(self, path: str) -> list[io.BytesIO]:
        pass
