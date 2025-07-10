# src/structurer.py

import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def estruturar_exame_laboratorial(texto: str) -> str:
    """
    Recebe o texto bruto do exame e retorna uma estrutura markdown com:
    - data do exame, data da coleta, metodologia
    - tabela de parâmetros: nome, valor, unidade, valores de referência (se houver)
    Pode ser usado para qualquer exame laboratorial.
    """
    llm = ChatOpenAI(
        api_key=openai_api_key,
        model="gpt-4.1-nano-2025-04-14",
        temperature=0.0,
        max_tokens=2048
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "Você é um especialista em exames laboratoriais e deve extrair informações estruturadas de laudos clínicos. Sempre que possível, organize os dados no seguinte template em markdown:"
            "\n\n"
            "# Exame Laboratorial\n"
            "**Data do Exame:** <data_do_exame>\n"
            "**Data da Coleta:** <data_da_coleta>\n"
            "**Metodologia:** <metodologia>\n\n"
            "## Parâmetros\n\n"
            "| Parâmetro | Resultado | Unidade | Valores de Referência |\n"
            "|-----------|-----------|---------|----------------------|\n"
            "| ...       | ...       | ...     | ...                  |\n\n"
            "Se algum dado não estiver presente no texto, deixe o campo em branco. O markdown deve ser limpo, sem explicações extras."
        ),
        (
            "human",
            "Texto do exame:\n\n{text}\n\nPor favor, extraia e estruture todas as informações possíveis conforme o template acima."
        )
    ])

    chain = prompt | llm
    resposta = chain.invoke({"text": texto})
    markdown = resposta.content.strip()
    return markdown
