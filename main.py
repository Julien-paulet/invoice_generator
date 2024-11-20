import argparse
from invoice_generator.pdf_creator import create_pdf_invoice
from invoice_generator.json_reader import read_json

def main():
    parser = argparse.ArgumentParser(description='Create a PDF invoice from JSON data.')
    parser.add_argument('--outputFileName', help='Output PDF file name.', default=None)
    parser.add_argument('--date', help='Invoice date in DD/MM/YYYY format.', default=None)
    parser.add_argument('--factureNumber', help='Invoice number.', default=None)
    parser.add_argument('--bonusRate', type=float, help='Bonus rate as a decimal.', default=0.0)
    parser.add_argument('--TVA', type=float, help='TVA rate as a percentage.', default=0)

    args = parser.parse_args()

    data = read_json()
    create_pdf_invoice(
        data,
        args.outputFileName,
        args.date,
        args.factureNumber,
        args.bonusRate,
        args.TVA,
    )

if __name__ == "__main__":
    main()