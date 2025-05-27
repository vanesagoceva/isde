from PIL import Image, ImageEnhance
from fastapi import FastAPI, UploadFile, File
from io import BytesIO
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.post("/transform-image/")
async def transform_image(
    file: UploadFile = File(...),
    color: float = 1.0,
    brightness: float = 1.0,
    contrast: float = 1.0,
    sharpness: float = 1.0
):
    image = Image.open(BytesIO(await file.read()))
    image = ImageEnhance.Color(image).enhance(color)
    image = ImageEnhance.Brightness(image).enhance(brightness)
    image = ImageEnhance.Contrast(image).enhance(contrast)
    image = ImageEnhance.Sharpness(image).enhance(sharpness)
    buf = BytesIO()
    image.save(buf, format="JPEG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/jpeg")
