# src/pdf_extractor.py

import fitz  # PyMuPDF

def extrair_texto_pdf(caminho_pdf: str) -> str:
    texto = ""
    with fitz.open(caminho_pdf) as pdf:
        for pagina in pdf:
            texto += pagina.get_text()
    return texto
