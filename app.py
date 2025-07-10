# app.py

import streamlit as st
from src.pdf_receiver import validar_pdf
from src.pdf_extractor import extrair_texto_pdf
from src.classifier import classificar_exame_laboratorial
from src.structurer import estruturar_exame_laboratorial
from src.fhir_generator import gerar_fhir_via_llm
import tempfile
import json

st.set_page_config(page_title="Processador de Exames Laboratoriais", layout="centered")

st.title("Envio e Processamento de Exame Laboratorial (PDF) para geração de recurso FHIR")

uploaded_file = st.file_uploader("Envie o arquivo PDF do exame", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        caminho_pdf = tmp_file.name

    # Validação
    if validar_pdf(caminho_pdf):
        texto = extrair_texto_pdf(caminho_pdf)
        st.success("Texto extraído com sucesso!")
        st.expander("Visualizar texto extraído").write(texto)

        if classificar_exame_laboratorial(texto):
            st.success("PDF classificado como exame laboratorial!")
            markdown = estruturar_exame_laboratorial(texto)
            st.expander("Markdown estruturado").markdown(markdown)

            st.info("Gerando recurso FHIR (pode demorar alguns segundos)...")
            fhir_json_str = gerar_fhir_via_llm(markdown)
            try:
                fhir_json = json.loads(fhir_json_str)
                st.json(fhir_json)
            except Exception:
                st.error("Não foi possível exibir o JSON FHIR completo (resposta truncada?).")
                st.code(fhir_json_str, language="json")
        else:
            st.warning("O arquivo não é um exame laboratorial. Tente outro PDF.")
    else:
        st.error("Arquivo PDF inválido ou muito grande.")

st.caption("Desenvolvido para interoperabilidade HL7 FHIR • IA em Saúde • 2025")

st.markdown("""
---
Dúvidas, críticas, sugestões?  
Entre em contato comigo através do meu LinkedIn [eliandrolima](https://www.linkedin.com/in/eliandrolima78)
""")