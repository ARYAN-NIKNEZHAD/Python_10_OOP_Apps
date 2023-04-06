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
        pass


the_bill = Bill(amount=120, period="March 2021")
john = FlatMate(name="John", days_in_house=20)
marry = FlatMate(name="Marry", days_in_house=25)

print(f"John pays: {john.pays(bill=the_bill, flatmate2=marry)}")
print(f"Marry pays: {marry.pays(bill=the_bill, flatmate2=john)}")
