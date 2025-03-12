import py7zr
import os
import csv
import shutil

def listar_pdfs(arquivo_7z):
    pdfs = []
    caminho_extracao = "documents/temps"
    
    with py7zr.SevenZipFile(arquivo_7z, mode='r') as arquivo:
        arquivos = arquivo.getnames()

        for f in arquivos:
            if f.lower().endswith('.pdf'):
                nome_pdf = os.path.basename(f)  # Remove o caminho
                nome_sem_extensao = os.path.splitext(nome_pdf)[0]  # Remove a extensão
                pdfs.append(nome_sem_extensao)
            
            elif f.lower().endswith(".7z"):
                arquivo.extract(targets=[f], path=caminho_extracao)  # Extrai o .7z interno
                
                # Processa o .7z extraído
                caminho_arquivo_extraido = os.path.join(caminho_extracao, f)
                pdfs.extend(listar_pdfs(caminho_arquivo_extraido))  # Chama a função recursivamente
    
    return pdfs

def salvar_csv(nomes, nome_csv):
    caminho_extracao = "documents/temps"
    # 🔥 Apagar a pasta temporária depois do uso
    if os.path.exists(caminho_extracao):
        shutil.rmtree(caminho_extracao)
    with open(nome_csv, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(["Nome do Arquivo"])  # Cabeçalho
        for nome in nomes:
            escritor.writerow([nome])

# Exemplo de uso
arquivo_7z = "documents/seven&sevenZip.7z"
nome_csv = "nomes_arquivos.csv"

pdfs_encontrados = listar_pdfs(arquivo_7z)
salvar_csv(pdfs_encontrados, nome_csv)

