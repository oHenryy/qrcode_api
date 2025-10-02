import io
from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import StreamingResponse, RedirectResponse
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import numpy as np
import cv2

app = FastAPI(
    title="API de QR Code",
    description="Uma API para gerar e processar QR Codes.",
    version="1.0.0"
)

@app.get("/", include_in_schema=False)
async def root():
    """
    Redireciona o usuário da rota raiz para a documentação da API.
    """
    return RedirectResponse(url="/docs")

@app.post("/gerar-qrcode/",
          summary="Gera uma imagem de QR Code",
          tags=["QR Code"])
async def gerar_qrcode(data: str = Form(..., description="O texto ou URL para incluir no QR Code.")):
    """
    Recebe um texto ou URL e gera uma imagem de QR Code em formato PNG.

    - **data**: O conteúdo que será codificado no QR Code.
    """

    img = qrcode.make(data)

    buf = io.BytesIO()
    img.save(buf, "PNG")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")

@app.post("/ler-qrcode/",
          summary="Processa uma imagem e lê o QR Code",
          tags=["QR Code"])
async def ler_qrcode(file: UploadFile = File(..., description="A imagem do QR Code para processar.")):
    """
    Recebe um arquivo de imagem (PNG, JPG, etc.), lê o QR Code e
    retorna os dados decodificados.
    """

    contents = await file.read()

    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    decoded_objects = decode(img)

    if not decoded_objects:
        return {"error": "Nenhum QR Code encontrado na imagem."}

    qr_data = decoded_objects[0].data.decode("utf-8")
    return {"data": qr_data}