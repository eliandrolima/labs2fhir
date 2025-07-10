# src/pdf_extractor.py

import fitz  # PyMuPDF
import pdfplumber

def extrair_texto_pdf(caminho_pdf: str) -> str:
    texto = ""
    with fitz.open(caminho_pdf) as pdf:
        for pagina in pdf:
            texto += pagina.get_text()
    return texto


def extrair_tabelas_pdf(caminho_pdf: str):
    tabelas = []
    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            tabelas_da_pagina = pagina.extract_tables()
            for tabela in tabelas_da_pagina:
                tabelas.append(tabela)
    return tabelas
