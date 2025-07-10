# src/fhir_mapper.py

import re
from datetime import datetime
import uuid

def parse_markdown_exame(markdown: str) -> dict:
    """
    Extrai campos do markdown padronizado para dicionário estruturado.
    """
    # Extrai datas e metodologia
    data_exame = re.search(r'\*\*Data do Exame:\*\*\s*(.*)', markdown)
    data_coleta = re.search(r'\*\*Data da Coleta:\*\*\s*(.*)', markdown)
    metodologia = re.search(r'\*\*Metodologia:\*\*\s*(.*)', markdown)

    # Extrai tabela de parâmetros (linha a linha)
    tabela = re.findall(r'\|([^\|]+)\|([^\|]+)\|([^\|]+)\|([^\|]+)\|', markdown)
    parametros = []
    for linha in tabela[1:]:  # Ignora header
        nome, resultado, unidade, referencia = [item.strip() for item in linha]
        if nome:
            parametros.append({
                "nome": nome,
                "resultado": resultado,
                "unidade": unidade,
                "referencia": referencia
            })
    return {
        "data_exame": data_exame.group(1).strip() if data_exame else "",
        "data_coleta": data_coleta.group(1).strip() if data_coleta else "",
        "metodologia": metodologia.group(1).strip() if metodologia else "",
        "parametros": parametros
    }

def gerar_fhir_exame(parsed: dict) -> dict:
    """
    Monta o DiagnosticReport e Observations em formato FHIR R4 (JSON).
    """
    # Gera Observations
    observations = []
    obs_refs = []
    for idx, param in enumerate(parsed["parametros"], 1):
        obs_id = f"obs-{idx}"
        # Códigos SNOMED/LOINC: usar dicionários, APIs ou fallback para codificações genéricas
        observation = {
            "resourceType": "Observation",
            "id": obs_id,
            "status": "final",
            "code": {
                "coding": [
                    {"system": "http://loinc.org", "code": "", "display": param["nome"]},  # preencher conforme evolução
                    {"system": "http://snomed.info/sct", "code": "", "display": param["nome"]},
                ],
                "text": param["nome"]
            },
            "valueQuantity": {
                "value": float(param["resultado"].replace(",", ".").split()[0]) if param["resultado"] else None,
                "unit": param["unidade"]
            },
            "referenceRange": [{
                "text": param["referencia"]
            }] if param["referencia"] else []
        }
        observations.append(observation)
        obs_refs.append({"reference": f"Observation/{obs_id}"})

    # Gera DiagnosticReport
    diagnostic_report = {
        "resourceType": "DiagnosticReport",
        "id": str(uuid.uuid4()),
        "status": "final",
        "category": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/v2-0074",
                "code": "LAB"
            }]
        }],
        "code": {
            "coding": [{
                "system": "http://loinc.org",
                "code": "58410-2",
                "display": "Laboratory studies"
            }]
        },
        "effectiveDateTime": parsed["data_exame"] or datetime.now().isoformat(),
        "issued": datetime.now().isoformat(),
        "result": obs_refs
    }

    # Retorna um bundle FHIR com o relatório e as observações
    return {
        "resourceType": "Bundle",
        "type": "collection",
        "entry": [
            {"resource": diagnostic_report},
            *[{"resource": obs} for obs in observations]
        ]
    }
