from io import BytesIO
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from core import solid_color_card
from models import ImageText


api_description = """
Project using Pillow to create and modify images, and FastAPI as API endpoint and WebSocket.
"""

app = FastAPI(
    title="Pillow's image generator",
    description=api_description,
    version="0.0.1",
    contact={
        "name": "Henrique Marchi",
        "url": "https://github.com/henrique-marchi",
        "email": "henriquemspro@gmail.com",
    }
)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/instant", tags=["incident"])
def instant_image(ia: ImageText) -> StreamingResponse:

    img = solid_color_card(ia)

    r_rgb = img.convert("RGB")
    response_image = BytesIO()

    r_rgb.save(response_image, "JPEG")
    response_image.seek(0)

    return StreamingResponse(response_image, media_type="image/jpeg")


