from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from datetime import datetime
import os

from .fonts import register_fonts

def create_pdf_invoice(data, output_file_name=None, date=None, facture_number=None, bonus_rate=0.0, TVA=0):
    # Register and configure fonts
    register_fonts()
    
    # Set default values
    date_obj = datetime.now() if not date else datetime.strptime(date, "%d/%m/%Y")
    date_str = date_obj.strftime("%d/%m/%Y")
    facture_number = facture_number or f"{date_obj.strftime('%d%m%Y')}-1"
    if output_file_name:
        output_file_name = f"outputs/{output_file_name}.pdf"
    else:
        output_file_name = f"outputs/Facture-{date_obj.strftime('%Y%m%d')}.pdf"

    # Create PDF canvas
    c = canvas.Canvas(output_file_name, pagesize=A4)
    width, height = A4

    # Use the registered font
    c.setFont('DejaVuSans', 12)

    # Add header with own information
    c.drawString(40, height - 60, data["info"]["name"])
    c.drawString(40, height - 80, data["info"]["address"])
    c.drawString(40, height - 100, f"{data['info']['postal_code']} {data['info']['city']}")
    c.drawString(40, height - 120, data["info"]["email"])
    c.drawString(40, height - 140, f"SIREN: {data['info']['siren']}")
    
    # Customer info - right aligned
    # First let's calculate the number of characters of the address (longest info in my opinion)
    max_length = len(data["info"]["customer"]["address"]) * 7 # *7 because a character is 7 times smaller than the width unit's of mesure
    customer_info_x = width - max_length
    c.drawString(customer_info_x, height - 60, "À l’attention de:")
    c.drawString(customer_info_x, height - 80, data["info"]["customer"]["name"])
    c.drawString(customer_info_x, height - 100, data["info"]["customer"]["address"])
    c.drawString(customer_info_x, height - 120, f"{data['info']['customer']['postal_code']} {data['info']['customer']['city']}")
    
    # Facture and Date
    c.drawString(40, height - 180, f"N° Facture: {facture_number}")
    c.drawString(customer_info_x, height - 180, f"Date: {date_str}")

    # Table Data
    table_data = [["Description", "Tarif Horaire", "Bonus performances", "Nombre d'heures", "Total"]]
    sous_total = 0

    # Iterate over each class to fill table rows
    for course_name, details in data["class"].items():
        hourly_rate = details["hourlyRate"]
        number_of_hours = details["numberOfHours"]
        class_amount = hourly_rate * (1 + bonus_rate) * number_of_hours
        sous_total += class_amount

        table_data.append([
            course_name,
            f"{hourly_rate}€",
            f"{bonus_rate * 100}%",
            f"{number_of_hours:.2f}",
            f"{class_amount:.2f}€"
        ])

    # Add a row for the total
    table_data.append(["", "", "", "Sous-Total", f"{sous_total:.2f}€"])

    # Create Table
    table = Table(table_data, colWidths=[180, 70, 110, 110, 80])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'DejaVuSans'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('LINEAFTER', (0, 0), (-1, -1), 1, colors.black),
        ('LINEBEFORE', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Draw the table
    table.wrapOn(c, width, height)
    table.drawOn(c, 40, height - 270)

    # Add a line for Total with TVA handling
    if TVA == 0:
        c.drawString(400, height - 380, f"Total Général : {sous_total:.2f} T.T.C")
        c.drawString(195, height - 400, "TVA non appréciable. Article 293B du code général des impôts")
    else:
        total_general = sous_total * (100+TVA)/100
        c.drawString(400, height - 380, f"Total Général : {total_general:.2f} T.T.C")
        c.drawString(400, height - 400, f"Taux de TVA {TVA}%")       

    # Footer: Bank details and conditions
    base_height = 460
    c.drawString(40, height - base_height, "Détails bancaires:")
    c.drawString(40, height - (base_height + 20), f"Banque: {data['info']['bank']}")
    c.drawString(40, height - (base_height + 40), f"IBAN: {data['info']['iban']}")
    c.drawString(40, height - (base_height + 60), f"Code SWIFT: {data['info']['swift']}")
    c.drawString(40, height - (base_height + 80), "Conditions: Paiement à réception")
    
    # Save the PDF
    c.save()