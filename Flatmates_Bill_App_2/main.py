from fpdf import FPDF
import webbrowser


class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class FlatMate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


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


the_bill = Bill(amount=120, period="March 2021")
john = FlatMate(name="John", days_in_house=20)
marry = FlatMate(name="Marry", days_in_house=25)

print(f"John pays: {john.pays(bill=the_bill, flatmate2=marry)}")
print(f"Marry pays: {marry.pays(bill=the_bill, flatmate2=john)}")

pdf_report = PdfReport("Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
