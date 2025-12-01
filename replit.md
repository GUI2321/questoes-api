# Banco de Questões Matemáticas API

## Visão Geral
API para geração automatizada de questões matemáticas organizadas por volume e tópico, com exportação para PDF e integração com Google Drive.

## Funcionalidades
- Geração de questões matemáticas com níveis (Fácil, Médio, Difícil)
- Tópicos suportados: Conjuntos, Funções, Equações
- Exportação automática para PDF formatado
- Upload automático para Google Drive (opcional)
- API REST compatível com GPT Custom Actions

## Estrutura do Projeto
```
/
├── main.py          # API FastAPI principal
├── gerador.py       # Lógica de geração de questões
├── pdf.py           # Geração de PDF com ReportLab
├── drive.py         # Integração com Google Drive
├── pdfs/            # Pasta onde os PDFs são salvos
├── requirements.txt # Dependências Python
└── pyproject.toml   # Configuração do projeto
```

## Endpoints da API

### GET /
Retorna informações sobre a API e endpoints disponíveis.

### GET /health
Verifica se a API está funcionando.

### GET /auth/google
Inicia o fluxo de autorização do Google Drive.

### GET /auth/status
Verifica se o Google Drive está autorizado.

### POST /gerar-questoes
Gera questões matemáticas e retorna PDF.

**Corpo da requisição:**
```json
{
  "volume": 1,
  "topico": "Conjuntos",
  "quantidade": 80,
  "salvarNoDrive": false
}
```

**Resposta:**
```json
{
  "status": "sucesso",
  "markdownContent": "# VOLUME 1...",
  "pdfUrl": "https://.../download/volume_1_Conjuntos.pdf",
  "mensagem": "Geradas 80 questões..."
}
```

### GET /download/{filename}
Faz download do PDF gerado.

## Como Usar com GPT Custom Actions

Cole este OpenAPI Spec no seu GPT:

```yaml
openapi: 3.1.0
info:
  title: Banco de Questões API
  version: 1.0.0
servers:
  - url: https://SEU-DOMINIO-AQUI
paths:
  /gerar-questoes:
    post:
      operationId: gerarQuestoes
      summary: Gera questões matemáticas e exporta como PDF
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                volume:
                  type: integer
                topico:
                  type: string
                quantidade:
                  type: integer
                salvarNoDrive:
                  type: boolean
      responses:
        '200':
          description: Questões geradas com sucesso
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                  markdownContent:
                    type: string
                  pdfUrl:
                    type: string
```

## Configuração do Google Drive
1. Acesse `/auth/google` para autorizar o acesso
2. Faça login com sua conta Google
3. Após autorizar, use `salvarNoDrive: true` nas requisições

## Dependências
- FastAPI - Framework web
- Uvicorn - Servidor ASGI
- ReportLab - Geração de PDFs
- Pydantic - Validação de dados
- google-api-python-client - API do Google Drive
- google-auth-oauthlib - Autenticação OAuth

## Variáveis de Ambiente (Secrets)
- GOOGLE_CLIENT_ID - ID do cliente OAuth do Google
- GOOGLE_CLIENT_SECRET - Secret do cliente OAuth do Google

## Mudanças Recentes
- 01/12/2025: Adicionada integração com Google Drive
- 01/12/2025: Criação inicial da API com geração de questões e PDFs
