import textwrap

from PIL import Image, ImageDraw, ImageFont


COLOR_BLACK = (0, 0, 0)
COLOR_PURPLE = (121, 23, 189)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (235, 96, 22)
COLOR_YELLOW = (251, 255, 0)
COLOR_BLUE = (0, 149, 255)
COLOR_LIGHT_GREEN = (24, 255, 0)
COLOR_DARK_GREEN = (0, 150, 10)


def break_text(text):
    return textwrap.fill(text, 11)


def create_backbone():
    img = Image.open("./backgrounds/models/backbone/backbone_black.png")
    width, height = img.size  # (3000, 1000)
    img_draw = ImageDraw.Draw(img)

    border_size = 50

    line_color = COLOR_BLACK
    line_width = 5

    txt_anchor = "mm"
    txt_align = "center"

    fnt = ImageFont.truetype("ARLRDBD.TTF", 30)
    fnt_dispair = ImageFont.truetype("ARLRDBD.TTF", 60)
    fnt_color = (0, 0, 0)

    img_draw.line((width - width, 180, width, 180), fill=line_color, width=15)  # header
    img_draw.line(
        (width - width, 1000, width, 1000), fill=line_color, width=line_width
    )  # footer

    img_draw.line((450, 180, 450, 1000), fill=line_color, width=line_width)  # coluna 1
    img_draw.line(
        (1500, 180, 1500, 1000), fill=line_color, width=line_width
    )  # coluna 2
    img_draw.line(
        (2000, 180, 2000, 1000), fill=line_color, width=line_width
    )  # coluna 3
    img_draw.line(
        (2350, 180, 2350, 1000), fill=line_color, width=line_width
    )  # coluna 4
    img_draw.line(
        (2700, 180, 2700, 1000), fill=line_color, width=line_width
    )  # coluna 5

    img_draw.line((450, 390, 1500, 390), fill=line_color, width=line_width)  # linha 1_1
    img_draw.line((450, 592, 1500, 592), fill=line_color, width=line_width)  # linha 1_2
    img_draw.line((450, 794, 1500, 794), fill=line_color, width=line_width)  # linha 1_3

    img_draw.line(
        (2000, 592, 2700, 592), fill=line_color, width=line_width
    )  # linha 2_1

    img_draw.multiline_text(
        (248, 215),
        "OCORRÊNCIA",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 1 linha 1
    img_draw.multiline_text(
        (976, 215),
        "TRECHO 1",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 2 linha 1
    img_draw.multiline_text(
        (976, 425),
        "TRECHO 2",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 2 linha 2
    img_draw.multiline_text(
        (976, 625),
        "TRECHO 3",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 2 linha 3
    img_draw.multiline_text(
        (976, 825),
        "TRECHO 4",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 2 linha 4
    img_draw.multiline_text(
        (1751, 215),
        "STATUS",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 3 linha 1
    img_draw.multiline_text(
        (2176, 230),
        break_text("AFETAÇÃO DIRETA"),
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 4 linha 1
    img_draw.multiline_text(
        (2176, 450),
        break_text("AFETAÇÃO INDIRETA"),
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 4 linha 1
    img_draw.multiline_text(
        (2176, 625),
        "CRITICIDADE",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 4 linha 3
    img_draw.multiline_text(
        (2526, 230),
        break_text("INÍCIO DO INCIDÊNTE"),
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 5 linha 1
    img_draw.multiline_text(
        (2526, 625), "SLA", align=txt_align, anchor=txt_anchor, fill=fnt_color, font=fnt
    )  # coluna 5 linha 1
    img_draw.multiline_text(
        (2877, 215), "URA", align=txt_align, anchor=txt_anchor, fill=fnt_color, font=fnt
    )  # coluna 6 linha 1

    width_80 = width * 0.8

    img_draw.multiline_text(
        (width_80 * 0.25, 25),
        "BACKBONE",
        align=txt_align,
        anchor=txt_anchor,
        fill=(255, 0, 0),
        font=fnt_dispair,
    )  # coluna 6 linha 1
    img_draw.multiline_text(
        (width_80 * 0.5, 25),
        "BACKBONE",
        align=txt_align,
        anchor=txt_anchor,
        fill=(255, 0, 0),
        font=fnt_dispair,
    )  # coluna 6 linha 1
    img_draw.multiline_text(
        (width_80 * 0.75, 25),
        "BACKBONE",
        align=txt_align,
        anchor=txt_anchor,
        fill=(255, 0, 0),
        font=fnt_dispair,
    )  # coluna 6 linha 1
    img_draw.multiline_text(
        (width_80, 25),
        "BACKBONE",
        align=txt_align,
        anchor=txt_anchor,
        fill=(255, 0, 0),
        font=fnt_dispair,
    )  # coluna 6 linha 1

    img_draw.multiline_text(
        (width_80 * 0.25, 1075),
        "BACKBONE",
        align=txt_align,
        anchor=txt_anchor,
        fill=(255, 0, 0),
        font=fnt_dispair,
    )  # coluna 6 linha 1
    img_draw.multiline_text(
        (width_80 * 0.5, 1075),
        "BACKBONE",
        align=txt_align,
        anchor=txt_anchor,
        fill=(255, 0, 0),
        font=fnt_dispair,
    )  # coluna 6 linha 1
    img_draw.multiline_text(
        (width_80 * 0.75, 1075),
        "BACKBONE",
        align=txt_align,
        anchor=txt_anchor,
        fill=(255, 0, 0),
        font=fnt_dispair,
    )  # coluna 6 linha 1
    img_draw.multiline_text(
        (width_80, 1075),
        "BACKBONE",
        align=txt_align,
        anchor=txt_anchor,
        fill=(255, 0, 0),
        font=fnt_dispair,
    )  # coluna 6 linha 1

    # img.save("./backgrounds/models/teste5.png")
    img.show()


def create_gpon(archive, color):
    img = Image.open(f"./backgrounds/models/gpon/{archive}.png")

    width, height = img.size  # (3000, 1000)
    border_size = 50

    line_color = color
    line_width = 6
    img_draw = ImageDraw.Draw(img)

    fnt = ImageFont.truetype("ARLRDBD.TTF", 30)
    slot_fnt = ImageFont.truetype("ARLRDBD.TTF", 25)
    fnt_color = (0, 0, 0)
    txt_anchor = "mm"
    txt_align = "center"

    img_draw.line((width - width, 180, width, 180), fill=line_color, width=15)  # header
    img_draw.line(
        (width - width, 1000, width, 1000), fill=line_color, width=line_width
    )  # footer

    img_draw.line((450, 180, 450, 1000), fill=line_color, width=line_width)  # coluna 1

    # img_draw.line((575, 180, 575, 1000), fill=line_color, width=line_witch)
    # img_draw.line((700, 180, 700, 1000), fill=line_color, width=line_witch)
    img_draw.line((800, 180, 800, 1000), fill=line_color, width=line_width)  # coluna 2
    img_draw.line((950, 180, 950, 1000), fill=line_color, width=line_width)  # coluna 3
    # img_draw.line((1075, 180, 1075, 1000), fill=line_color, width=line_witch)
    # img_draw.line((1200, 180, 1200, 1000), fill=line_color, width=line_witch)   # coluna 4

    img_draw.line((450, 592, 1300, 592), fill=line_color, width=line_width)  # linha 2_1

    img_draw.line(
        (1300, 180, 1300, 1000), fill=line_color, width=line_width
    )  # coluna 5
    img_draw.line(
        (2000, 180, 2000, 1000), fill=line_color, width=line_width
    )  # coluna 6
    img_draw.line(
        (2350, 180, 2350, 1000), fill=line_color, width=line_width
    )  # coluna 7
    img_draw.line(
        (2700, 180, 2700, 1000), fill=line_color, width=line_width
    )  # coluna 8

    img_draw.line(
        (2000, 592, 2700, 592), fill=line_color, width=line_width
    )  # linha 2_1

    img_draw.multiline_text(
        (248, 215),
        "OCORRÊNCIA",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 1 linha 1
    img_draw.multiline_text(
        (626, 215), "POP", align=txt_align, anchor=txt_anchor, fill=fnt_color, font=fnt
    )  # coluna 2 linha 1
    img_draw.multiline_text(
        (626, 450), "OLT", align=txt_align, anchor=txt_anchor, fill=fnt_color, font=fnt
    )  # coluna 4 linha 1
    img_draw.multiline_text(
        (876, 215),
        "PLACA",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 3 linha 1
    img_draw.multiline_text(
        (1126, 215), "PON", align=txt_align, anchor=txt_anchor, fill=fnt_color, font=fnt
    )  # coluna 4 linha 1
    img_draw.multiline_text(
        (1651, 215),
        "REGIÃO",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 5 linha 1

    img_draw.multiline_text(
        (626, 625), "POP", align=txt_align, anchor=txt_anchor, fill=fnt_color, font=fnt
    )  # coluna 4 linha 3
    img_draw.multiline_text(
        (626, 860), "OLT", align=txt_align, anchor=txt_anchor, fill=fnt_color, font=fnt
    )  # coluna 4 linha 3
    img_draw.multiline_text(
        (876, 625),
        "PLACA",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 4 linha 3
    img_draw.multiline_text(
        (1126, 625), "PON", align=txt_align, anchor=txt_anchor, fill=fnt_color, font=fnt
    )  # coluna 4 linha 3

    img_draw.multiline_text(
        (2176, 230),
        break_text("AFETAÇÃO DIRETA"),
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 4 linha 1
    img_draw.multiline_text(
        (2176, 625),
        "CRITICIDADE",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 4 linha 3
    img_draw.multiline_text(
        (2526, 230),
        break_text("INÍCIO DO INCIDÊNTE"),
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )  # coluna 5 linha 1
    img_draw.multiline_text(
        (2526, 625), "SLA", align=txt_align, anchor=txt_anchor, fill=fnt_color, font=fnt
    )  # coluna 5 linha 1
    img_draw.multiline_text(
        (2877, 215), "URA", align=txt_align, anchor=txt_anchor, fill=fnt_color, font=fnt
    )  # coluna 6 linha 1

    img.save(f"./backgrounds/models/gpon/{archive}.png")
    img.show()


def insert_logo(img, brand):
    logo = Image.open(f"./backgrounds/models/logos/{brand}.png")  # 216 x 110
    img.paste(logo, (60, 55), logo)
    # img.save("./backgrounds/models/gpon/test_gpon_vip.png")
    img.show()


def insert_img(archive):
    img = Image.open(f"./backgrounds/models/gpon/{archive}.png")
    alert = Image.open("./backgrounds/models/alert_yellow100.png").convert(
        "RGBA"
    )  # 216 x 110
    img.paste(alert, (2930, 65), alert)

    al = "_alert"

    img.save(f"./backgrounds/models/gpon/{archive}.png")
    img.show()


def create_instant():
    img = Image.open("./backgrounds/models/instant/instant_blue.png")

    width, height = img.size  # (2000, 1000)
    border_size = 50

    line_color = COLOR_BLUE
    line_width = 6
    img_draw = ImageDraw.Draw(img)

    fnt = ImageFont.truetype("ARLRDBD.TTF", 30)
    title_fnt = ImageFont.truetype("ARLRDBD.TTF", 80)
    fnt_color = (0, 0, 0)
    txt_anchor = "mm"
    txt_align = "center"

    img_draw.line((width - width, 180, width, 180), fill=line_color, width=15)  # header

    img_draw.line((1249, 180, 1249, 1000), fill=line_color, width=line_width)
    img_draw.line((1649, 180, 1649, 1000), fill=line_color, width=line_width)
    img_draw.line((2049, 180, 2049, 1000), fill=line_color, width=line_width)

    img_draw.multiline_text(
        (width / 2, 115),
        "ALERTA INSTANTÂNEO",
        align=txt_align,
        anchor=txt_anchor,
        fill=line_color,
        font=title_fnt,
    )
    img_draw.multiline_text(
        (648, 230),
        "REGIÃO / OLT",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )
    img_draw.multiline_text(
        (1450, 230),
        break_text("AFETADOS DIRETAMENTE"),
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )
    img_draw.multiline_text(
        (1850, 230),
        "HORÁRIO DE INÍCIO",
        align=txt_align,
        anchor=txt_anchor,
        fill=fnt_color,
        font=fnt,
    )

    img_draw.line((width - width, 280, width, 280), fill=line_color, width=15)  # header
    img_draw.line((width - width, 1000, width, 1000), fill=line_color, width=line_width)

    img.save("./backgrounds/models/instant/instantaneous.png")

    img.show()


create_gpon("gpon_dark_green", COLOR_DARK_GREEN)
