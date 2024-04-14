from fpdf import FPDF
import pyfiglet


def Procceing_PDF_file(bg, fg, font_family, font_size, font_style, text, file_name):
    pdf = FPDF()
    pdf.add_page()

    if not bg.strip():
        bg_list = (255, 255, 255)
    else:
        bg_list = list(map(int, bg.split(",")))
    pdf.set_fill_color(*bg_list)
    pdf.rect(0, 0, 210, 297, "F")

    if not fg.strip():
        fg_list = (0, 0, 0)
    else:
        fg_list = list(map(int, fg.split(",")))
    pdf.set_text_color(*fg_list)

    if not font_family.strip():
        font_family = "Times"

    if not font_size.strip():
        font_size = 10

    pdf.set_font(font_family, size=(int(font_size)), style=font_style)

    pdf.multi_cell(width(int(font_size)), height(int(font_size)), txt=text, align="L")

    if not file_name.strip():
        file_name = "example"
    pdf_output_file = file_name + ".pdf"

    pdf.output(pdf_output_file)
    print()
    print("A PDF has been successfully created at this name ->", pdf_output_file)
    print()


text = "PDF Creater!"
ascii_art = pyfiglet.figlet_format(text, font="standard")
print(ascii_art)

text = input("Enter the text: ")
bg = input("Enter the Background color(RGB): ")
fg = input("Enter the Font color(RGB): ")
font_family = input("Enter the Font family(Arial, Times, Courier, Helvetica): ")
font_size = input("Enter the Font size: ")
font_style = input("Enter the Font style(B,I,U): ")
file_name = input("Enter the only file name(file_name): ")


def height(font_size):
    if font_size <= 10:
        return 5
    if font_size <= 15:
        return 7
    if font_size <= 20:
        return 9
    if font_size <= 25:
        return 11
    if font_size <= 30:
        return 13
    if font_size <= 35:
        return 15
    else:
        return 25


def width(font_size):
    if font_size <= 10:
        return 190
    if font_size <= 15:
        return 190
    if font_size <= 20:
        return 190
    if font_size <= 25:
        return 190
    if font_size <= 30:
        return 190
    if font_size <= 35:
        return 190
    else:
        return 190


Procceing_PDF_file(bg, fg, font_family, font_size, font_style, text, file_name)
