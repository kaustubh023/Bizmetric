class Validations:

    @staticmethod
    def validate_subject(subjects):
        while True:
            subject = input("Select Subject (HR / Finance / Marketing / DS): ").upper()
            if subject in subjects:
                return subject
            print("Invalid Subject!")

    @staticmethod
    def validate_input(message):
        while True:
            value = input(message).upper()
            if value in ['Y', 'N']:
                return value
            print("Enter Y or N only!")

    @staticmethod
    def validate_number(message):
        while True:
            try:
                num = int(input(message))
                if num >= 0:
                    return num
                print("Must be positive.")
            except ValueError:
                print("Invalid number!")

    @staticmethod
    def validate_transport():
        while True:
            t = input("Transportation (ANNUAL / SEMESTER): ").upper()
            if t in ['ANNUAL', 'SEMESTER']:
                return t
            print("Invalid transport option.")
