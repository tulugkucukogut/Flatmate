from flat import Bill, Flatmate
from report import PdfReport


bill_amount = int(input("Hey user, enter the Bill amount"))
period = input("What is the Bill period?")

the_bill = Bill(bill_amount, period)


name1 = input("What is your name")
house_day = int(input("How many days you will stay?"))
flatmate1 = Flatmate(name=name1,days_in_house=house_day)

name2 = input("What is your name")
house_day2 = int(input("How many days you will stay?"))
flatmate2 = Flatmate(name=name2,days_in_house=house_day2)

print("f'{} pays: ".format(flatmate1), flatmate1.pays(the_bill,flatmate1))
print("f'{} pays: ".format(flatmate2), flatmate1.pays(the_bill,flatmate1))

pdf_report = PdfReport("hi.pdf")
pdf_report.generate(flatmate1,flatmate2,the_bill)