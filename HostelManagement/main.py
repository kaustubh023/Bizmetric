from database import Database
from master_course import MasterCourse

def main():
    course = MasterCourse()
    course.calculate_total()
    
    

try:
    main()
except Exception as e:
    print("Application Error:", e)
