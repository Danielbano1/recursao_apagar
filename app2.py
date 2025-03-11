import py7zr
import os
import csv

def listar_pdfs(arquivo_7z):
    with py7zr.SevenZipFile(arquivo_7z, mode='r') as arquivo:
        arquivos = arquivo.getnames()
        pdfs = [os.path.splitext(f)[0] for f in arquivos if f.lower().endswith('.pdf')]
    return pdfs

def salvar_csv(nomes, nome_csv):
    with open(nome_csv, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(["Nome do Arquivo"])  # Cabeçalho
        for nome in nomes:
            escritor.writerow([nome])

# Exemplo de uso
arquivo_7z = "documents/variosSeven.7z"
nome_csv = "nomes_arquivos.csv"

pdfs_encontrados = listar_pdfs(arquivo_7z)
salvar_csv(pdfs_encontrados, nome_csv)