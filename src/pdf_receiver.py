import os

def validar_pdf(caminho_pdf: str, tamanho_max_mb: float = 1.0) -> bool:
    if not os.path.isfile(caminho_pdf):
        print("Arquivo não encontrado.")
        return False
    if not caminho_pdf.lower().endswith('.pdf'):
        print("Arquivo não é um PDF.")
        return False
    tamanho_mb = os.path.getsize(caminho_pdf) / (1024 * 1024)
    if tamanho_mb > tamanho_max_mb:
        print(f"Arquivo excede o limite de {tamanho_max_mb} MB.")
        return False
    return True