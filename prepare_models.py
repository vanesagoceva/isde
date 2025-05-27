import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image
from fastapi import FastAPI, UploadFile, File
from io import BytesIO

app = FastAPI()

model_dict = {
    "resnet18": models.resnet18(pretrained=True),
    "vgg16": models.vgg16(pretrained=True),
    "efficientnet_b0": models.efficientnet_b0(pretrained=True)
}

@app.post("/predict/")
async def predict(model_name: str, file: UploadFile = File(...)):
    model = model_dict.get(model_name)
    if model is None:
        return {"error": "Model not found"}
    model.eval()
    image = Image.open(BytesIO(await file.read())).convert("RGB")
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
    ])
    input_tensor = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        output = model(input_tensor)
    _, predicted = torch.max(output, 1)
    return {"predicted_class": predicted.item()}
