class Student():
    def __init__(self, name, age, roll, year, cgpa):
        self.name = name
        self.age = age
        self.roll = roll
        self.year = year
        self.cgpa = cgpa


class StudentManagement():
    def __init__(self):
        self.students = []
    
    def clear_students(self):
        self.students = []

    # This method validates if the input is empty or not and raises an exception if it is empty
    def validate_empty_input(self, value):
        if value:
            return value
        else:
            raise Exception("Input cannot be empty")

    def validate_unique_name(self, name):
        # First validate, if the input is empty or not
        self.validate_empty_input(name)

        # Now it validates if the name is alphabets or not, then it checks if the name already exists or not
        if name.isalpha():
            print("Name is alphabets")
            for student in self.students:
                if student.name == name:
                    raise Exception("Name already exists")
            return name
        else:
            raise Exception("Name must be alphabets")

    # This method does the same thing as validate_unique_name, but for roll
    def validate_unique_roll(self, roll):
        self.validate_empty_input(roll)

        for student in self.students:
            if student.roll == roll:
                raise Exception("Roll already exists")
        return roll

    def accept_student(self, name=None, age=None, roll=None, year=None, cgpa=None):
        # This validates the input and returns the validated input if there is no error
        name = self.validate_unique_name(name)
        age = self.validate_empty_input(age)
        roll = self.validate_unique_roll(roll)
        year = self.validate_empty_input(year)
        cgpa = self.validate_empty_input(cgpa)

        student = Student(name, age, roll, year, cgpa)
        self.students.append(student)
        return

    def display_students(self):
        students = ""
        for student in self.students:
            students += f"{student.name} {student.age} {student.roll} {student.year} {student.cgpa} "
        return students

    def search_student(self, roll):
        for student in self.students:
            if student.roll == roll:
                return f"{student.name} {student.age} {student.roll} {student.year} {student.cgpa}"
        return "Student not found"

    def delete_student(self, roll):
        for student in self.students:
            if student.roll == roll:
                self.students.remove(student)
                return f"{student.name} {student.age} {student.roll} {student.year} {student.cgpa}"
        return "Student not found"

    def update_student(self, roll, name=None, age=None, year=None, cgpa=None):
        for student in self.students:
            if student.roll == roll:
                student.name = name
                student.age = age
                student.year = year
                student.cgpa = cgpa
                return
        return "Student not found"