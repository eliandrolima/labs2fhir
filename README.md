# 🧬 NLP2FHIR: Extração de Exames Laboratoriais em FHIR

**NLP2FHIR** é uma aplicação Python que automatiza a extração, classificação e padronização de resultados de exames laboratoriais em PDF para o padrão internacional HL7 FHIR R4, utilizando inteligência artificial e técnicas avançadas de NLP.

## 🚀 Visão Geral

Este projeto visa facilitar a interoperabilidade de dados clínicos, convertendo laudos laboratoriais não estruturados em PDFs em recursos FHIR estruturados e codificados (SNOMED-CT), prontos para integração com prontuários eletrônicos e outras soluções de saúde digital.

---

## 🛠️ Funcionalidades Principais

* **Upload de PDF** com resultados laboratoriais
* **Extração robusta** do texto e tabelas do PDF
* **Classificação automática** (LLM) para validar se o arquivo contém exames laboratoriais
* **Estruturação dos dados** (NLP/LLM) em formato padronizado (data, metodologia, parâmetros, resultados, unidades, valores de referência)
* **Mapeamento automático para FHIR** (Observation, DiagnosticReport, etc), incluindo codificação SNOMED-CT quando aplicável
* **Saída em JSON FHIR puro**, pronto para integração

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nlp2fhir.git
cd nlp2fhir
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

> **Obs:** Será necessário configurar uma chave de API da OpenAI para uso dos LLMs.

---

## ⚡ Uso Básico

### Linha de Comando (exemplo inicial)

```bash
python src/main.py --pdf_path "exemplo_exame.pdf"
```

* O sistema extrairá, classificará e converterá o PDF em um JSON FHIR, exibindo o resultado puro.

---

## 🔄 Fluxo da Aplicação

1. **Recebimento do PDF**
2. **Extração de texto e tabelas**
3. **Classificação do conteúdo (LLM)**
4. **Estruturação dos dados (LLM/NLP)**
5. **Mapeamento e geração do recurso FHIR**
6. **Exibição do JSON FHIR**

---

## 🧩 Principais Dependências

* `PyMuPDF` ou `pdfplumber` (extração PDF)
* `LangChain`, `OpenAI` (LLM/NLP)
* `fhir.resources` (manipulação FHIR)
* `pytest` (testes automatizados)

Veja o arquivo `requirements.txt` para a lista completa.

---

## 🔒 Segurança & Privacidade

* Todos os dados processados localmente
* Não armazena exames ou dados sensíveis após a execução
* Recomenda-se uso em ambiente seguro e controlado

---

## 📝 Exemplos de Uso

Veja a pasta [`examples/`](examples/) para PDFs de exemplo e JSONs gerados.

---

## 💡 Contribuição

Pull requests são bem-vindos!
Consulte o [CONTRIBUTING.md](CONTRIBUTING.md) para diretrizes e reporte problemas via [Issues](https://github.com/seu-usuario/nlp2fhir/issues).

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## ✨ Roadmap

* [ ] Interface Web (Streamlit ou FastAPI)
* [ ] Internacionalização (i18n)
* [ ] Suporte a múltiplos tipos de laudos laboratoriais
* [ ] Otimização para nuvem (Docker, AWS)

---

## 📬 Contato

Dúvidas, sugestões ou consultoria?
Abra uma issue ou entre em contato pelo email: **[eliandrolima@me.com](mailto:eliandrolima@me.com)**
LinkedIn: **[eliandrolima78](https://www.linkedin.com/in/eliandrolima78)**

