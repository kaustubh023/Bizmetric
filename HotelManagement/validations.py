class Validate():
    
    @staticmethod
    def correct_string(value):
        if not value.isalpha() :
            raise ValueError("Your Input is wrong , put only Alphabets")
        return value.strip()
        
        
        
    @staticmethod
    def correct_number(value):
        if float(value) <=0 :
            raise ValueError("You Enter wrong Input ")
        return float(value)
    