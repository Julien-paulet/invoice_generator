# Invoice Generator

This is a Python-based invoice generator that creates PDF invoices from JSON data. It uses the `reportlab` library to generate well-structured and customizable invoices.


## Features

- Reads invoice details from JSON files.
- Supports specifying a custom bonus rate and TVA.
- Uses command-line arguments to easily customize the invoice details.
- Generates PDF invoices in a professional layout.
- Supports customizable fonts for a better presentation.


## Prerequisites

- Python 3.x
- `reportlab` library


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Julien-paulet/invoice_generator.git
   cd invoice_generator

2. **Install the required Python packages:**

It's recommended to use a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the dependencies:**

pip install -r requirements.txt
Ensure font files (DejaVuSans.ttf and DejaVuSans-Bold.ttf) are in the "sources/font/" directory. You can obtain these from the DejaVu Fonts website.


## Usage
To generate an invoice from a JSON file, run the following command:

cd path/to/this/folder
python main.py --outputFileName Invoice.pdf --date 08/11/2024 --bonusRate 0.45 --TVA 20
Command-line Arguments
jsonFilePath: Path to the JSON file containing invoice data.
--outputFileName: The name of the output PDF file (optional, default is "Facture-CurrentDate.pdf").
--date: Invoice date in %d/%m/%Y format (optional, default is current date).
--factureNumber: Custom invoice number (optional, default is "CurrentDate-1").
--bonusRate: Bonus rate as a decimal for the calculations (optional, default: 0.0).
--TVA: TVA rate as a percentage (optional, default: 0).


## JSON Format
Your JSON file should be structured like this:

{
    "info": {
        "name": "Your Name",
        "address": "Your Address",
        "postal_code": "12345",
        "city": "Your City",
        "email": "your.email@example.com",
        "siren": "XXXXXXX",
        "iban": "FR76 XXXX XXXX XXXX XXXX XXXX XXX",
        "bank": "Your Bank",
        "swift": "SWIFTXXX",
        "customer": {
            "name": "Customer Name",
            "address": "Customer Address",
            "postal_code": "54321",
            "city": "Customer City"
        }
    },
    "class": {
        "Course Name": {
            "hourlyRate": 20,
            "numberOfHours": 5
        }
    }
}

And it should be saved under "/sources/json/facture_data.json"

** NOTE : You can add multiple class (though the output pdf might look ugly if you go over 3) **

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for potential improvements and fixes.


## License
This project is licensed under the MIT License - see the LICENSE file for details.