# src/main.py (fragmento)
import json
from pdf_receiver import validar_pdf
# from pdf_extractor import extrair_texto_pdf, extrair_tabelas_pdf
from pdf_extractor import extrair_texto_pdf
from classifier import classificar_exame_laboratorial
from structurer import estruturar_exame_laboratorial
# from fhir_mapper import parse_markdown_exame, gerar_fhir_exame
from fhir_generator import gerar_fhir_via_llm

caminho = "exames/hemograma.pdf"

if __name__ == "__main__":
    # caminho = input("Informe o caminho do PDF: ")
    if validar_pdf(caminho):
        texto = extrair_texto_pdf(caminho)
        #tabelas = extrair_tabelas_pdf(caminho)
        print("Texto extraído com sucesso!")
        print(texto)
        # print(tabelas)
        # Próximos passos: classificação e estruturação



        if classificar_exame_laboratorial(texto):
            print("PDF classificado como exame laboratorial. Prosseguindo...")
            markdown = estruturar_exame_laboratorial(texto)
            print("\n--- MARKDOWN ESTRUTURADO ---\n")
            print(markdown)
            # parsed = parse_markdown_exame(markdown)
            # fhir_json = gerar_fhir_exame(parsed)
            fhir_json = gerar_fhir_via_llm(markdown)
            print(fhir_json)  # Não coloque textos antes/depois (p/ aderir ao padrão do pipeline)
            # print(json.dumps(fhir_json, indent=2, ensure_ascii=False))
        else:
            print("O arquivo PDF NÃO contém um exame laboratorial. Encerrando fluxo.")


    else:
        print("PDF inválido.")

