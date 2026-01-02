# 📄 PDF Utility — Ferramenta Profissional para Manutenção de PDFs

Este projeto é uma **ferramenta utilitária em Python**, desenvolvida para realizar **manutenção e manipulação prática de arquivos PDF** de forma centralizada, simples e eficiente.

Não se trata de um projeto de estudo ou demonstração acadêmica.  
Este é um **projeto real**, criado para resolver necessidades recorrentes de trabalho com documentos PDF.

---

## 🎯 Objetivo

Centralizar operações comuns de manutenção de PDFs em uma única aplicação local, reduzindo dependência de múltiplas ferramentas externas e processos manuais.

O foco é **produtividade**, **clareza de uso** e **manutenibilidade do código**.

---

## 🧠 Abordagem Técnica

A solução foi construída com uma abordagem pragmática:

- Interface simples e funcional
- Código modular por tipo de operação
- Baixa complexidade acidental
- Facilidade de evolução incremental
- Execução local, sem dependência de serviços externos

Cada funcionalidade foi isolada em módulos próprios, facilitando manutenção e extensões futuras.

---

## 🗂️ Estrutura do Projeto

```
utility-doc/
├── requirements.txt
├── LICENSE.txt
├── README.md
└── utility-doc/
    ├── images/
    │   └── logo.png
    ├── src/
    │   ├── app.py
    │   ├── utilidades.py
    │   ├── menu_unir.py
    │   ├── menu_reduzir.py
    │   ├── menu_extrair.py
    │   ├── menu_imagens.py
    │   ├── menu_marca_dagua.py
    │   └── menu_converte_prn.py
    └── tools/
        └── DOSPrinter.exe
```

### Principais Componentes

- **app.py**  
  Ponto de entrada da aplicação. Orquestra a interface e os menus.

- **menu_*.py**  
  Cada arquivo representa um conjunto específico de operações sobre PDFs, mantendo separação clara de responsabilidades.

- **utilidades.py**  
  Funções auxiliares compartilhadas entre os módulos.

- **tools/**  
  Ferramentas auxiliares necessárias para funcionalidades específicas.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Streamlit** — interface web local
- **Bibliotecas de manipulação de PDF**
- **Bibliotecas de processamento de imagem**

As dependências completas estão listadas em `requirements.txt`.

---

## ⚙️ Instalação

### Pré-requisitos

- Python 3.9 ou superior
- Ambiente virtual (recomendado)

### Clonar o repositório

```bash
git clone https://github.com/<seu-usuario>/pdf-utility.git
cd pdf-utility
```

### Criar ambiente virtual

```bash
python -m venv venv
```

Ativar o ambiente:

- Windows:
```bash
venv\Scripts\activate
```

- Linux / macOS:
```bash
source venv/bin/activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Execução

Com o ambiente ativo, execute:

```bash
streamlit run utility-doc/src/app.py
```

A aplicação será aberta automaticamente no navegador padrão.

---

## 🧩 Funcionalidades

Entre as funcionalidades disponíveis estão:

- União de arquivos PDF
- Redução/compactação de PDFs
- Extração de páginas
- Manipulação de imagens em documentos PDF
- Aplicação de marca d’água
- Conversões específicas de documentos

As funcionalidades são acessadas por meio de menus claros e organizados.

---

## 📌 Contexto Profissional

Este projeto representa uma solução prática para um problema real e recorrente.  
Não busca demonstrar complexidade técnica desnecessária, mas **capacidade de entregar soluções úteis, organizadas e sustentáveis**.

Projetos como este refletem maturidade técnica: saber quando **simplificar** é a melhor decisão de engenharia.

---

## 🚧 Status

Projeto funcional e em uso, com evolução conforme surgem novas demandas.

---

## 📄 Licença

Distribuído sob licença conforme especificado em `LICENSE.txt`.
