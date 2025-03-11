from typing import Iterable
from pathlib import PurePath

from classifications.abc_compression_extention_classifier import ABCCompressionExtensionClassifier, CompressionExtension

class ByNameCompressionExtensionClassifier(ABCCompressionExtensionClassifier):
    def classify(self, path: str) -> CompressionExtension:
        ext = PurePath(path).suffix.replace(".", "").lower()
        if ext == CompressionExtension.SEVENZIP.value:
            return CompressionExtension.SEVENZIP
        elif ext == CompressionExtension.ZIP.value:
            return CompressionExtension.ZIP
        elif ext == CompressionExtension.TAR.value:
            return CompressionExtension.TAR
        else:
            return CompressionExtension.UNKNOWN
        
    def classify_multiple(self, paths: Iterable[str]) -> dict[str, CompressionExtension]:
        classifications = {}
        for path in paths:
            classifications[path] = self.classify(path)
        return classifications