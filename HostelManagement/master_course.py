from validations import Validations
from database import Database


class MasterCourse:

    def __init__(self):
        self.subjects = ['HR', 'FINANCE', 'MARKETING', 'DS']
        self.core_fee = 200000
        self.analytics_fee = 0.10 * self.core_fee
        self.hostel_fee = 200000
        self.food_per_month = 2000
        self.transport_per_sem = 13000

    def calculate_total(self):

        try:
            total_cost = 0
            
            student_name = input("Enter Student Name: ").strip().title()
            subject = Validations.validate_subject(self.subjects)
            total_cost += self.core_fee

            if subject == "DS":
                analytics = "N"
            else:
                analytics = Validations.validate_input("Do you want Analytics (Y/N): ")
                if analytics == "Y":
                    total_cost += self.analytics_fee

            hostel = Validations.validate_input(" do you want Hostel (Y/N): ")
            if hostel == "Y":
                total_cost += self.hostel_fee

            months = Validations.validate_number("You want food for how many months : ")
            total_cost += months * self.food_per_month

            transport = Validations.validate_transport()
            if transport == "ANNUAL":
                total_cost += self.transport_per_sem * 2
            else:
                total_cost += self.transport_per_sem

            
            Database.insert_record(
                (student_name, subject, analytics, hostel, months, transport, total_cost)
             )

            self.generate_bill(student_name,subject, analytics, hostel, months, transport, total_cost)

        except Exception as e:
            print("Calculation Error:", e)

   

    def generate_bill(self, student_name, subject, analytics, hostel, months, transport, total):

        try:
            file_name = "Fee_Receipt.txt"

            width = 60

            with open(file_name, "w", encoding="utf-8") as file:

                file.write("\n")
                file.write("+" + "-"*(width-2) + "+\n")
                file.write("|{:^58}|\n".format("MASTER COURSE FEE RECEIPT"))
                file.write("+" + "-"*(width-2) + "+\n")

                file.write("| {:<25}: {:>28} |\n".format("Student Name", student_name))
                file.write("| {:<25}: {:>28} |\n".format("Subject", subject))
                file.write("| {:<25}: {:>28} |\n".format("Analytics", analytics))
                file.write("| {:<25}: {:>28} |\n".format("Hostel", hostel))
                file.write("| {:<25}: {:>28} |\n".format("Food Months", months))
                file.write("| {:<25}: {:>28} |\n".format("Transport", transport))

                file.write("+" + "-"*(width-2) + "+\n")
                file.write("| {:<25}: ₹{:>26,.2f} |\n".format("TOTAL AMOUNT", total))
                file.write("+" + "-"*(width-2) + "+\n")

            print("\nBill successfully generated")

        except Exception as e:
            print("Bill generation error:", e)

