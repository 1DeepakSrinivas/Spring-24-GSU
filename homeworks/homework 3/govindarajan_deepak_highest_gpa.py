class Student():
    def __init__(self,fname,lname,gpa):
        self.fname = fname
        self.lname = lname
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa
    
    def get_first(self):
        return self.fname
    
    def get_last(self):
        return self.lname

    
class Course():
    def __init__(self,roster):
        self.roster = roster

    def add_student(self,student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)

    def find_student_highest_gpa(self):
        try:
            max_gpa = 0
            highest_gpa_student = None
            for student in self.roster:
                if student.get_gpa() > max_gpa:
                    max_gpa = student.get_gpa()
                    highest_gpa_student = student
            if highest_gpa_student is None:
                raise EmptyRosterError
            return highest_gpa_student
        except EmptyRosterError:
            print("The roster is empty.")

class EmptyRosterError(Exception):
    def error(self):
        return "Exception. Course Roster is Empty."

def main():
    course = Course([])
    print("Welcome to CSC/DSCI 1301: Principles in CS/DS I")
    while True:
        print("Please Add Students to the Course: (quit or q to exit)\n")
        first_name = input("Enter First Name: ")
        if first_name.lower() in ['quit', 'q']:
            if course.course_size() > 0:
                try:
                    highest_gpa_student = course.find_student_highest_gpa()
                    print(f"\nTop Student: {highest_gpa_student.get_first()} {highest_gpa_student.get_last()} (GPA: {highest_gpa_student.get_gpa()})")
                except EmptyRosterError as e:
                    print(e)
            print(f"Course Size: {course.course_size()} students.")
            break
        last_name = input("Enter Last Name: ")
        gpa = input("Enter GPA: ")
        try:
            student = Student(first_name, last_name, float(gpa))
            course.add_student(student)
        except ValueError:
            print("Error. Enter a Numeric GPA.")

main()
        
        
        
