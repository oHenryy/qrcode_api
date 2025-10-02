# API de Geração e Leitura de QR Code

Esta é uma API simples e eficiente desenvolvida com **FastAPI** para realizar duas funções principais:

1.  **Gerar** imagens de QR Code a partir de um texto ou URL.
2.  **Ler** o conteúdo de um QR Code a partir do upload de uma imagem.

A API conta com documentação interativa automática (via Swagger UI) para facilitar os testes e a integração.

## ✨ Features

  - [x] Geração de QR Code em formato PNG.
  - [x] Leitura de QR Codes de imagens (PNG, JPG, etc.).
  - [x] Endpoint raiz (`/`) que redireciona para a documentação.
  - [x] Documentação interativa automática com Swagger UI e ReDoc.
  - [x] Estrutura assíncrona para alta performance.

## 🛠️ Tecnologias Utilizadas

  - **Backend:** [Python 3](https://www.python.org/)
  - **Framework API:** [FastAPI](https://fastapi.tiangolo.com/)
  - **Servidor ASGI:** [Uvicorn](https://www.uvicorn.org/)
  - **Geração de QR Code:** `qrcode` com `Pillow`
  - **Leitura de QR Code:** `pyzbar` e `OpenCV-Python`

## 🚀 Configuração do Ambiente

Siga os passos abaixo para executar o projeto localmente.

### 1\. Clone o repositório

```bash
# Clone este repositório (ou crie a pasta do projeto)
git clone https://github.com/oHenryy/qrcode_api.git
cd qrcode_api
```

### 2\. Crie e ative um ambiente virtual

É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

  * **Linux/macOS:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
  * **Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### 3\. Instale as dependências

O arquivo `requirements.txt` contém todas as bibliotecas necessárias.

```bash
pip install -r requirements.txt
```

## ▶️ Como Executar a API

Com o ambiente configurado e as dependências instaladas, inicie o servidor Uvicorn:

```bash
uvicorn main:app --reload
```

  - `main`: refere-se ao arquivo `main.py`.
  - `app`: refere-se ao objeto `app = FastAPI()` criado no arquivo.
  - `--reload`: reinicia o servidor automaticamente após qualquer alteração no código.

A API estará disponível no endereço: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

## 📖 Uso da API

Para testar e interagir com a API, acesse a documentação interativa gerada automaticamente pelo FastAPI:

**[http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)**

### Endpoints Disponíveis

#### 1\. Gerar QR Code

  - **Endpoint:** `POST /gerar-qrcode/`
  - **Descrição:** Gera uma imagem de QR Code com base nos dados fornecidos.
  - **Entrada:** `form-data` com um campo `data` (string).
  - **Resposta de Sucesso:** Uma imagem no formato `image/png`.

**Exemplo de uso com cURL:**

```bash
curl -X POST "http://127.0.0.1:8000/gerar-qrcode/" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "data=https%3A%2F%2Fwww.google.com" \
--output qrcode_gerado.png
```

*(Este comando irá salvar a imagem do QR code gerado no arquivo `qrcode_gerado.png`)*

-----

#### 2\. Ler QR Code

  - **Endpoint:** `POST /ler-qrcode/`
  - **Descrição:** Processa um arquivo de imagem, lê o QR Code contido nela e retorna o conteúdo.
  - **Entrada:** `multipart/form-data` com um campo `file`.
  - **Resposta de Sucesso:** Um objeto JSON com o conteúdo do QR Code.
    ```json
    {
      "data": "https://www.google.com"
    }
    ```
  - **Resposta de Erro:** Um objeto JSON com uma mensagem de erro.
    ```json
    {
      "error": "Nenhum QR Code encontrado na imagem."
    }
    ```

**Exemplo de uso com cURL:**

```bash
curl -X POST "http://127.0.0.1:8000/ler-qrcode/" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@/caminho/para/qrcode_gerado.png"
```

*(Substitua `/caminho/para/qrcode_gerado.png` pelo caminho real do arquivo da imagem)*