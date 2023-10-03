from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageOps
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


def break_text(text, letter_per_line) -> str:
    return textwrap.fill(text=text, width=letter_per_line)


def create_solid_color_image(size: tuple, background_color: (int, int, int), border: bool = False, border_color: (int, int, int) = COLOR_BLACK):
    img = Image.new(mode="RGBA", size=size, color=background_color)
    
    if not border:
        return img

    border_size = 20

    end_img = ImageOps.expand(img, border=border_size, fill=border_color)

    return end_img
    

def create_gradient_color_image(size: tuple, background_color):
    img = Image.new(mode="RGBA", size=size, color=background_color)
    return img


def solid_color_card(data: ImageText):
    img = create_solid_color_image(size=DEFAULT_IMAGE_SIZE, background_color=COLOR_BLUE, border=True)
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


def gradient_color_card(data: ImageText):
    img = create_gradient_color_image(size=DEFAULT_IMAGE_SIZE, background_color=COLOR_BLUE)
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


def user_image_card(data: ImageText, image):
    img = Image.open(image)
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
