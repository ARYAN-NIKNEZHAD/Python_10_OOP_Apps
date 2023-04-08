import webbrowser
import os
from fpdf import FPDF


class PdfReport:
    """
    Create a Pdf file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def generate(self, flatmate1, flatmate2, bill):
        flatmate_pay_1 = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate_pay_2 = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add icon
        pdf.image(
            name="files/house.png",
            w=30, h=30
        )

        # Add Title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate_pay_1, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate_pay_2, border=0, ln=1)

        # Change directory to files, generate and open the PDF
        os.chdir("files")
        pdf.output(self.file_name)
        webbrowser.open(self.file_name)
