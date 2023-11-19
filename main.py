from fpdf import FPDF
class Bill:
    def __init__(self,amount,period):
        self.amount = amount
        self.period = period

class Flatmate:
    def __init__(self,name,days_in_house):
        self.name = name
        self.days_in_house = days_in_house
    
    def pays(self,bill,flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = weight * bill.amount
        return to_pay
    

class PdfReport:
    def __init__(self,filename):
        self.filename = filename

    def generate(self):
        pdf = FPDF(orientation='P',unit='pt', format='A4')
        pdf.set_font(family='Times', size=24, style="B")
        pdf.add_page()
        pdf.cell(w=0, h= 88 , txt="Flatmates Bill", border=0, align="C", ln=1)
        pdf.cell(w=100, h= 88 , txt="Period", border=0, align="C")
        pdf.cell(w=150, h= 88 , txt="March 2021", border=0, align="C")
        pdf.output("bill.pdf")
the_bill = Bill(amount = 120, period="March 2021")
john = Flatmate(name="John",days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print("John pays: ", john.pays(the_bill,marry))
print("Marry pays: ", marry.pays(the_bill,john))

pdf_report = PdfReport("hi")
pdf_report.generate()