import webbrowser
from fpdf import FPDF
    

class PdfReport:
    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatmate1,flatmate2,bill):
        flatmate1_pay = str(round(flatmate1.pays(bill,flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill,flatmate1),2))

        pdf = FPDF(orientation='P',unit='pt', format='A4')
        pdf.set_font(family='Times', size=24, style="B")
        pdf.add_page()
        pdf.image("sidebar.png",w=30,h=30)
        pdf.cell(w=0, h= 88 , txt="Flatmates Bill", border=0, align="C", ln=1)
        pdf.set_font(family='Times', size=14, style="B")
        pdf.cell(w=100, h= 88 , txt="Period", border=0, align="C")
        pdf.cell(w=150, h= 88 , txt=bill.period, border=0, align="C", ln=1)


        pdf.cell(w=100, h= 40 , txt=flatmate1.name, border=0, align="C")
        pdf.cell(w=150, h= 40 , txt=flatmate1_pay, border=0, align="C", ln=1)

        pdf.cell(w=100, h= 40 , txt=flatmate2.name, border=0, align="C")
        pdf.cell(w=150, h= 40 , txt=flatmate2_pay, border=0, align="C")


        pdf.output(self.filename)
        webbrowser.open(self.filename)