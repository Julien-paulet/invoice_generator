from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

def register_fonts():
    font_name = 'DejaVuSans'
    font_bold = 'DejaVuSans-Bold'
    font_path = './sources/font/DejaVuSans.ttf'
    if not os.path.exists(font_path):
        raise FileNotFoundError("Font not found; ensure DejaVuSans is installed in the system fonts.")
    
    pdfmetrics.registerFont(TTFont(font_name, font_path))
    pdfmetrics.registerFont(TTFont(font_bold, font_path))