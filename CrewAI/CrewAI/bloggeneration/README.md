# **Projeto de Geração Automática de Posts de Blog a partir de PDFs**  

## **Descrição do Projeto**  

Este projeto automatiza a geração de posts de blog no formato Markdown a partir de arquivos PDF. Ele utiliza inteligência artificial (IA) para extrair, processar e transformar o conteúdo dos PDFs em posts estruturados e prontos para publicação.  

O sistema funciona por meio de um pipeline que:  
1. Lê arquivos PDF de um diretório específico.  
2. Extrai o texto contido nos PDFs.  
3. Processa o conteúdo extraído para criar uma estrutura organizada.  
4. Gera posts de blog em formato Markdown com base no conteúdo processado.  

---

## **Como Funciona**  

O projeto segue uma abordagem modular baseada em agentes inteligentes e tarefas sequenciais:  

1. **Agente de Leitura de PDF**:  
   - Responsável por ler o conteúdo dos arquivos PDF.  
   - Utiliza a biblioteca `pdfplumber` para extrair texto página por página, além de `crewai` e `crewai-tools` para análise e geração dos posts em Markdown por meio de agentes, tarefas e tools.  

2. **Agente de Processamento de Conteúdo**:  
   - Analisa o texto extraído e identifica as seções mais relevantes.  
   - Organiza o conteúdo para facilitar a criação do post.  

3. **Agente de Criação de Post**:  
   - Transforma o conteúdo processado em um post de blog estruturado.  
   - Formata o texto em Markdown, garantindo que ele esteja pronto para publicação.  

4. **Pipeline Sequencial**:  
   - Os agentes trabalham em conjunto, passando informações entre si até gerar o resultado final.  

---

## **Como Usar**  

### **Pré-requisitos**  
1. **Python 3.11**: Certifique-se de que o Python está instalado no seu sistema.  
2. **Dependências**: Instale as dependências do projeto executando:  
   ```
   pip install -r bloggeneration/requirements.txt
   ```  

### **Passo a Passo**  

#### **1. Configuração da API do Gemini**  
- Obtenha sua chave de API (`API Key`) para o modelo Gemini.  
- Crie um arquivo `.env` na raiz do projeto e adicione a chave da seguinte forma:  
  ```
  GOOGLE_API_KEY=sua_chave_api_aqui
  ```  

#### **2. Adicionar Arquivos PDF**  
- Coloque os arquivos PDF que deseja processar na pasta `pdfs/`.  
  - Certifique-se de que os arquivos estejam no formato `.pdf`.  

#### **3. Executar o Projeto**  
- Para rodar o sistema, utilize o comando:  
  ```
  python bloggeneration/src/bloggeneration/main.py
  ```  
- O sistema irá:  
  1. Procurar todos os arquivos PDF na pasta `pdfs/`.  
  2. Processar cada PDF e gerar um arquivo Markdown correspondente.  
  3. Salvar os arquivos Markdown na pasta `markdowns/`.  

#### **4. Verificar os Resultados**  
- Após a execução, os posts de blog gerados estarão disponíveis na pasta `markdowns/`.  
- Cada arquivo terá o mesmo nome do PDF original, mas com a extensão `.md`.  

---

## **Estrutura do Projeto**  

```
bloggeneration/
├── knowledge/              # Pasta para armazenar conhecimento relacionado  
├── pdfs/                   # Pasta para armazenar arquivos PDF  
├── src/  
│   ├── bloggenartion/       # Diretório principal do código-fonte  
│   │   ├── __pycache__/     # Arquivos compilados do Python  
│   │   ├── config/          # Configurações do projeto  
│   │   │   ├── agents.yaml  # Configuração de agentes  
│   │   │   ├── tasks.yaml   # Configuração de tarefas  
│   │   ├── tools/           # Ferramentas auxiliares  
│   │   │   ├── __init__.py  # Arquivo de inicialização do pacote  
│   │   ├── crew.py          # Script principal para gerenciamento da equipe de IA  
│   │   ├── main.py          # Script principal do projeto  
├── .env                     # Arquivo de configuração do ambiente  
├── .gitignore               # Arquivo para ignorar arquivos no Git  
├── pyproject.toml           # Configuração do projeto Python
└── requirements.txt         # Dependências do projeto  
├── README.md                # Documentação do projeto  
├── markdowns/               # Pasta onde os arquivos Markdown gerados serão salvos  
```  

---

## **Exemplo de Uso**  

### **Entrada**  
Coloque um arquivo chamado `exemplo.pdf` na pasta `pdfs/`.  

### **Saída**  
Após a execução, será gerado um arquivo `exemplo.md` na pasta `markdowns/`, contendo o post de blog formatado em Markdown.  

---

## **Dicas e Melhores Práticas**  

1. **Organize seus PDFs**:  
   - Certifique-se de que os arquivos PDF estão bem estruturados e legíveis.  
   - Evite PDFs com imagens escaneadas ou textos não selecionáveis.  

2. **Personalize o Modelo**:  
   - Ajuste os parâmetros do modelo Gemini no arquivo `crew.py` para melhorar a qualidade do texto gerado.  

---

## **Limitações**  

- O sistema funciona melhor com PDFs que contêm texto simples e bem estruturado.  
- PDFs com imagens escaneadas ou textos complexos podem não ser processados corretamente.  
- A qualidade do texto gerado depende do modelo de IA utilizado.  

---