import io
import os
import py7zr
from abc_compressed_documents import ABCCompressedDocuments

class SevenZipDocumentExtractor(ABCCompressedDocuments):

    def extract(self, path: str) -> list[io.BytesIO]:
        documents = [".pdf",]
        bytes_list = list()
        
        with py7zr.SevenZipFile(path, mode='r') as file:
            extracted_files = file.read()
            for file_name, content_bytes in extracted_files.items():
                if os.path.splitext(file_name)[1].lower() in documents:
                    bytes_list.append(content_bytes)
                    

        return bytes_list