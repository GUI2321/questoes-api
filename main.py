from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel
from gerador import gerar_questoes
from pdf import salvar_pdf
from drive import get_auth_url, exchange_code_for_token, upload_para_drive, is_drive_authorized
import os

app = FastAPI(
    title="Banco de Questões Matemáticas API",
    description="API para geração automatizada de questões matemáticas organizadas por volume e tópico, com exportação para PDF e integração com Google Drive.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequisicaoQuestoes(BaseModel):
    volume: int
    topico: str
    quantidade: int
    salvarNoDrive: bool = False


@app.get("/")
async def root():
    drive_status = "Autorizado" if is_drive_authorized() else "Não autorizado (acesse /auth/google)"
    return {
        "mensagem": "Bem-vindo à API de Banco de Questões Matemáticas!",
        "google_drive": drive_status,
        "endpoints": {
            "POST /gerar-questoes": "Gera questões matemáticas e retorna PDF",
            "GET /health": "Verifica status da API",
            "GET /auth/google": "Autoriza acesso ao Google Drive",
            "GET /download/{filename}": "Baixa um PDF gerado"
        }
    }


@app.get("/health")
async def health():
    return {"status": "ok", "mensagem": "API funcionando corretamente"}


@app.get("/auth/google")
async def auth_google():
    try:
        auth_url, state = get_auth_url()
        return RedirectResponse(url=auth_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao iniciar autenticação: {str(e)}")


@app.get("/oauth2callback")
async def oauth_callback(code: str = None, error: str = None):
    if error:
        raise HTTPException(status_code=400, detail=f"Erro na autenticação: {error}")
    
    if not code:
        raise HTTPException(status_code=400, detail="Código de autorização não recebido")
    
    try:
        exchange_code_for_token(code)
        return {
            "status": "sucesso",
            "mensagem": "Google Drive autorizado com sucesso! Agora você pode usar salvarNoDrive: true"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao trocar código por token: {str(e)}")


@app.get("/auth/status")
async def auth_status():
    return {
        "google_drive_autorizado": is_drive_authorized()
    }


@app.post("/gerar-questoes")
async def gerar_questoes_endpoint(req: RequisicaoQuestoes):
    if req.quantidade < 1 or req.quantidade > 200:
        raise HTTPException(
            status_code=400,
            detail="Quantidade deve estar entre 1 e 200 questões"
        )
    
    if not req.topico.strip():
        raise HTTPException(
            status_code=400,
            detail="Tópico não pode estar vazio"
        )
    
    try:
        questoes_markdown = gerar_questoes(
            volume=req.volume,
            topico=req.topico,
            quantidade=req.quantidade
        )
        
        pdf_path = salvar_pdf(req.volume, req.topico, questoes_markdown)
        
        if req.salvarNoDrive:
            if not is_drive_authorized():
                raise HTTPException(
                    status_code=401,
                    detail="Google Drive não autorizado. Acesse /auth/google primeiro para autorizar."
                )
            try:
                pdf_url = upload_para_drive(pdf_path)
            except Exception as e:
                raise HTTPException(
                    status_code=500,
                    detail=f"Erro ao enviar para o Google Drive: {str(e)}"
                )
        else:
            domain = os.environ.get("REPLIT_DEV_DOMAIN", "")
            if domain:
                pdf_url = f"https://{domain}/download/{os.path.basename(pdf_path)}"
            else:
                pdf_url = f"http://localhost:5000/download/{os.path.basename(pdf_path)}"
        
        return {
            "status": "sucesso",
            "markdownContent": questoes_markdown,
            "pdfUrl": pdf_url,
            "mensagem": f"Geradas {req.quantidade} questões do Volume {req.volume} - {req.topico}"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao gerar questões: {str(e)}"
        )


@app.get("/download/{filename}")
async def download_pdf(filename: str):
    filepath = f"pdfs/{filename}"
    
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="PDF não encontrado")
    
    return FileResponse(
        filepath,
        media_type="application/pdf",
        filename=filename
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
