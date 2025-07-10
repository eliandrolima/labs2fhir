# src/classifier.py

import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

def classificar_exame_laboratorial(texto: str) -> bool:
    llm = ChatOpenAI(
        api_key=openai_api_key,
        model="gpt-4.1-nano-2025-04-14", # se quiser troque por outro modelo
        temperature=0.0,
        max_tokens=5
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um especialista em análise de exames laboratoriais."),
        ("human", "O texto abaixo corresponde a um resultado de exame laboratorial? Responda apenas SIM ou NÃO.\n\nTexto:\n{text}")
    ])

    chain = prompt | llm
    resposta = chain.invoke({"text": texto})
    resultado = resposta.content.strip().upper()
    return resultado == "SIM"
