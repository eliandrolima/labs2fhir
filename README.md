# 🧬 LABS2FHIR: Conversão de Exames Laboratoriais de PDFs para FHIR - v0.0.1

**LABS2FHIR** é uma aplicação teste em Python que automatiza a extração, classificação e padronização de resultados de exames laboratoriais em PDF para o padrão internacional HL7 FHIR R4, utilizando inteligência artificial e técnicas avançadas de NLP.

## 🚀 Visão Geral

Este projeto visa testar a capacidade dos LLMs de transformar dados não estruturados, como textos com resultados de exames laboratoriais, em recursos FHIR estruturados e codificados (LOINC e SNOMED-CT) no formato json, deixando-os prontos para integração com outras soluções de saúde digital.

Este é apenas o primeiro teste. Com a evolução do projeto novas funções e características serão implementadas.

---

## 🛠️ Funcionalidades Principais

* **Upload de PDF** com contendo resultados de exames laboratoriais
* **Extração robusta** do texto do PDF
* **Classificação automática** (LLM) para validar se o arquivo contém realmente exames laboratoriais
* **Estruturação dos dados** (NLP/LLM) em formato padronizado (data, metodologia, parâmetros, resultados, unidades, valores de referência)
* **Mapeamento automático para FHIR** (Observation, DiagnosticReport, etc), incluindo codificação SNOMED-CT quando aplicável
* **Saída de recurso FHIR**, em JSON puro

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/eliandrolima/labs2fhir.git
cd labs2fhir
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> **Obs:** Será necessário configurar uma chave de API da OpenAI para uso dos LLMs e incluí-la em um arquivo `.env`. Veja o exemplo no arquivo `.env.exemplo`.

---

## ⚡ Uso Básico

### Página Web rodando localmente

```bash
streamlit run app.py
```
> **Obs:** Normalmente a página abre automaticamente e roda na porta 8501 (http://localhost:8501)

* No local indicado, arraste e solte o PDF ou selecione-o a partir de seu diretório.
* O sistema extrairá, classificará e converterá o PDF em um recurso FHIR, exibindo o resultado em JSON puro.

> 🚨 **ALERTA IMPORTANTÍSSIMO**: O CONTEÚDO DO PDF SERÁ ENVIADO PARA PROCESSAMENTO NA OPENAI, PORTANTO CERTIFIQUE-SE DE QUE O PDF UTILIZADO ESTEJA DEVIDAMENTE ANONIMIZADO OU QUE VOCÊ TENHA AUTORIZAÇÃO EXPLÍCITA DO DONO DO EXAME LABORATORIAL PARA FAZER OS TESTE.

---

## 🔄 Fluxo da Aplicação

1. **Recebimento do PDF**
2. **Extração de texto**
3. **Classificação do conteúdo (LLM)**
4. **Estruturação dos dados (LLM/NLP)**
5. **Mapeamento e geração do recurso FHIR (LLM)**
6. **Exibição do JSON FHIR**

---

## 🧩 Principais Dependências

* `dotenv` (variáveis de ambiente)
* `PyMuPDF` (extração PDF)
* `LangChain` (LLM/NLP)
* `Streamlit` (UI)
* 

Veja o arquivo `requirements.txt` para a lista completa.


## 📬 Contato

Dúvidas, sugestões ou críticas?
Entre em contato através do meu LinkedIn: **[eliandrolima78](https://www.linkedin.com/in/eliandrolima78)**

