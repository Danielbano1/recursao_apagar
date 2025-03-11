import tarfile
import os
import io
from abc_compressed_documents import ABCCompressedDocuments

class TarDocumentExtractor(ABCCompressedDocuments):

    def extract(path: str) -> list[io.BytesIO]:
        documents = [".pdf",]
        bytes_list = list()
        
        with tarfile.open(path, mode='r:*') as file:
            for membro in file.getmembers():
                if membro.isfile() and os.path.splitext(membro.name)[1].lower() in documents:
                    content_bytes = io.BytesIO(file.extractfile(membro).read())
                    bytes_list.append(content_bytes)
        
        return bytes_list