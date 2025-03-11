import io   
from abc_compressed_documents import ABCCompressedDocuments
from classifications.abc_compression_extention_classifier import CompressionExtension
from classifications.by_name_compression_extention_classifier import ByNameCompressionExtensionClassifier
from sevenZip_document_extractor import SevenZipDocumentExtractor 
from zip_document_extractor import ZipDocumentExtractor
from tar_document_extractor import TarDocumentExtractor
from typing import Iterable




class CompressedDocumentExtractor():
    def __init__(self):
        self._handlers: dict[CompressionExtension, ABCCompressedDocuments] = {
            CompressionExtension.SEVENZIP: SevenZipDocumentExtractor(),
            CompressionExtension.ZIP: ZipDocumentExtractor(), 
            CompressionExtension.TAR: TarDocumentExtractor(),
        }
    
    def extract(self, path: str) -> list[io.BytesIO]:
        classifier = ByNameCompressionExtensionClassifier()
        extension = classifier.classify(path)
        if extension in self._handlers:
            handler = self._handlers[extension]
            return handler.extract(path)
        
    def extract_multiple(self, paths: Iterable[str]) -> dict[str, io.BytesIO]:
        extract_documents = {}
        for path in paths:
            extract_documents[path] = self.extract(path)
        return extract_documents
        



