
from fastapi import Request

class ClassificationForm:
    def __init__(self, request: Request):
        self.request = request
        self.image_id = None
        self.model_id = None

    async def load_data(self):
        form = await self.request.form()
        self.image_id = form.get("image_id")
        self.model_id = form.get("model_id")
