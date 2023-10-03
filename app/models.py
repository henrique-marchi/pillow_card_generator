from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class ImageText(BaseModel):
    text: str
