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

# Exemplo de uso:
if __name__ == "__main__":
    caminho = input("Informe o caminho do arquivo PDF: ")
    if validar_pdf(caminho):
        print("Arquivo validado com sucesso.")
    else:
        print("Arquivo inválido. Tente novamente.")
