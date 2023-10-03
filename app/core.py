from PIL import Image, ImageDraw, ImageFont
import re
import textwrap

from models import ImageText

COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 149, 255)
COLOR_DARK_GREEN = (0, 150, 10)
COLOR_LIGHT_GREEN = (24, 255, 0)
COLOR_ORANGE = (235, 96, 22)
COLOR_PURPLE = (121, 23, 189)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (251, 255, 0)
COLOR_WHITE = (255, 255, 255)

DEFAULT_ANCHOR = "mm"
DEFAULT_ALIGN = "center"

DEFAULT_FONT = ImageFont.truetype("./fonts/Roboto/Roboto-Regular.ttf", 45)
DEFAULT_IMAGE_HEIGHT = 1000
DEFAULT_IMAGE_WIDTH = 500
DEFAULT_IMAGE_SIZE = (DEFAULT_IMAGE_HEIGHT, DEFAULT_IMAGE_WIDTH)
DEFAULT_IMAGE_SIZE_10 = (DEFAULT_IMAGE_HEIGHT*10, DEFAULT_IMAGE_WIDTH*10)


def break_text(text, letter_per_line) -> str:
    return textwrap.fill(text=text, width=letter_per_line)


def create_image(size: tuple, background_color):
    img = Image.new(mode="RGBA", size=size, color=background_color)
    return img


def populate_image(data: ImageText):
    img = create_image(size=DEFAULT_IMAGE_SIZE, background_color=COLOR_BLUE)
    img_draw = ImageDraw.Draw(img)

    text = break_text(text=data.text, letter_per_line=40)

    img_draw.multiline_text(
        (DEFAULT_IMAGE_HEIGHT/2, DEFAULT_IMAGE_WIDTH/2), 
        text, 
        align=DEFAULT_ALIGN, 
        anchor=DEFAULT_ANCHOR, 
        font=DEFAULT_FONT, 
        fill=COLOR_WHITE
    )

    return img
