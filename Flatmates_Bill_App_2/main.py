from fpdf import FPDF
import webbrowser

from Flatmates_Bill_App_2.flat import Bill, FlatMate


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
            name="D:\\Python_project_for_git\\Python10OopApps\\python_10_oop_apps\\Flatmates_Bill_App_2\\files\\house.png",
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

        pdf.output(self.file_name)
        webbrowser.open(self.file_name)


amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? :")

name1 = input("What is your name? ")
days_in_house = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

the_bill = Bill(amount=amount, period=period)
flatmate1 = FlatMate(name=name1, days_in_house=days_in_house)
flatmate2 = FlatMate(name=name2, days_in_house=days_in_house2)

print(f"{flatmate1.name} pays: {flatmate1.pays(bill=the_bill, flatmate2=flatmate2)}")
print(f"{flatmate2.name} pays: {flatmate2.pays(bill=the_bill, flatmate2=flatmate1)}")

pdf_report = PdfReport(file_name=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
