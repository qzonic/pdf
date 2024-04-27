#!/usr/local/bin/python3.11
# -*- coding: utf-8 -*

# import csv
# import codecs
#
# with codecs.open('az-most_users.csv', "r", "utf_8_sig") as csvfile:
#     file = csv.reader(csvfile, delimiter=',', quotechar='|')
#     i = 0
#     for row in file:
#         if row[-1] != '""':
#             print(row[-1].replace('"', ''))
#             i += 1
#     print(i)

import os, sys

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))

file_name = "dst/0ae590b0bf761c237ee866b287a10a80.pdf"

def makepdf():
    pdf_file = "dst/0ae590b0bf761c237ee866b287a10a80.pdf"
    watermark = 'dst/compressed-0b1fb858682eeb67f2d7ca767657006a.pdf'
    merged = "Watermarked.pdf"

    with open(pdf_file, "rb") as input_file, open(watermark, "rb") as watermark_file:
        input_pdf = PdfReader(input_file)
        watermark_pdf = PdfReader(watermark_file)
        watermark_page = watermark_pdf.pages[0]

        output = PdfWriter()

        for i in range(len(input_pdf.pages)):
            pdf_page = input_pdf.pages[i]
            pdf_page.merge_page(watermark_page)
            output.add_page(pdf_page)

        with open(merged, "wb") as merged_file:
            output.write(merged_file)

makepdf()

def makeWatermark():
    text1 = '«© Произведение создано в рамках Программы по развитию личностного потенциала Благотворительного фонда "Вклад в будущее" (Россия) (далее – Фонд).'
    text2 = 'Исключительные права на произведение принадлежат Фонду. Произведение скачал(а): «Указание на ФИО» инициатора процесса скачивания»'
    with open("mark.png") as mark:
        pdf = canvas.Canvas(file_name, pagesize=A4)
        pdf.translate(inch, inch)
        print(pdf.getAvailableFonts())
        pdf.setFillColor(colors.grey, alpha=0.6)
        pdf.setFont("DejaVuSans", 6)
        pdf.drawCentredString(200, 10, text1)
        pdf.drawCentredString(177, 0, text2)
        # pdf.drawImage("mark.png", 0, 0)
        pdf.save()


# makeWatermark()

