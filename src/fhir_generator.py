# src/fhir_generator.py

import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def gerar_fhir_via_llm(markdown: str) -> str:
    """
    Recebe um markdown estruturado de exame laboratorial e retorna um FHIR Bundle (JSON)
    contendo DiagnosticReport e Observations, já com códigos SNOMED-CT e LOINC apropriados.
    """
    llm = ChatOpenAI(
        api_key=openai_api_key,
        model="gpt-4.1-nano-2025-04-14",  # Ajuste conforme necessário
        temperature=0.0,
        max_tokens=32768
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "Você é um expert em interoperabilidade em saúde. Sua tarefa é converter resultados de exames laboratoriais (fornecidos em markdown padronizado) em um FHIR Bundle no padrão HL7 FHIR R4, com recursos DiagnosticReport e Observations apropriados. "
            "Adicione sempre que possível os códigos corretos LOINC e SNOMED-CT para cada parâmetro analisado e para o exame como um todo. "
            "Se não souber algum código, deixe o campo de código vazio, mas nunca invente códigos. "
            "A saída deve ser APENAS o JSON puro do FHIR Bundle, sem explicações, comentários ou formatação adicional."
        ),
        (
            "human",
            "Aqui está o markdown do exame:\n\n{markdown}\n\nConverta para um FHIR Bundle JSON, incluindo todos os parâmetros como Observations e um DiagnosticReport, e utilize SNOMED-CT/LOINC sempre que aplicável. Responda apenas com o JSON."
        )
    ])

    chain = prompt | llm
    resposta = chain.invoke({"markdown": markdown})
    fhir_json = resposta.content.strip()
    return fhir_json
