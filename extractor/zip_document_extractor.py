import zipfile
import os
import io
from abc_compressed_documents import ABCCompressedDocuments

class ZipDocumentExtractor(ABCCompressedDocuments):

    def extract(path: str) -> list[io.BytesIO]:
        documents = [".pdf",]
        bytes_list = list()
        
        with zipfile.ZipFile(path, mode='r') as file:
            for file_name in file.namelist():
                if os.path.splitext(file_name)[1].lower() in documents:
                    with file.open(file_name) as extracted_files:
                        content_bytes = io.BytesIO(extracted_files.read())
                        bytes_list.append(content_bytes)
        
        return bytes_list