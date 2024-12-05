class Student:
    def __init__(self, name, student_id, email):
        self.name = name
        self.student_id = student_id
        self.email = email
        self.is_graduated = False

    def graduate(self):
        self.is_graduated = True

    def __str__(self):
        status = "Graduated" if self.is_graduated else "Enrolled"
        return f"Student: {self.name}, ID: {self.student_id}, Email: {self.email}, Status: {status}"


class Faculty:
    def __init__(self, name, field):
        self.name = name
        self.field = field
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def graduate_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id and not student.is_graduated:
                student.graduate()
                return f"Student {student.name} has graduated."
        return "Student not found or already graduated."

    def get_current_students(self):
        return [student for student in self.students if not student.is_graduated]

    def get_graduates(self):
        return [student for student in self.students if student.is_graduated]

    def student_in_faculty(self, student_id):
        return any(student.student_id == student_id for student in self.students)

    def __str__(self):
        return f"Faculty: {self.name}, Field: {self.field}, Total Students: {len(self.students)}"


class University:
    def __init__(self, name):
        self.name = name
        self.faculties = []

    def create_faculty(self, name, field):
        new_faculty = Faculty(name, field)
        self.faculties.append(new_faculty)
        return new_faculty

    def find_student_faculty(self, student_id):
        for faculty in self.faculties:
            if faculty.student_in_faculty(student_id):
                return faculty
        return None

    def display_faculties(self):
        for faculty in self.faculties:
            print(faculty)

    def display_faculties_by_field(self, field):
        for faculty in self.faculties:
            if faculty.field == field:
                print(faculty)


if __name__ == "__main__":
    university_name = input("Enter the name of the university: ")
    tum = University(university_name)

    num_faculties = int(input("Enter the number of faculties: "))
    faculties = []

    for _ in range(num_faculties):
        faculty_name = input("Enter faculty name: ")
        field = input("Enter field of study: ")
        faculties.append(tum.create_faculty(faculty_name, field))

    num_students = int(input("Enter the number of students: "))

    for _ in range(num_students):
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        email = input("Enter student email: ")
        faculty_choice = int(input("Choose a faculty by number (0 to {}): ".format(len(faculties) - 1)))
        if 0 <= faculty_choice < len(faculties):
            faculties[faculty_choice].enroll_student(Student(student_name, student_id, email))
        else:
            print("Invalid faculty choice.")

    graduate_id = input("Enter the student ID to graduate: ")
    print(tum.faculties[0].graduate_student(graduate_id))

    print("\nCurrent students in {}:".format(faculties[0].name))
    for student in faculties[0].get_current_students():
        print(student)

    print("\nGraduates in {}:".format(faculties[0].name))
    for student in faculties[0].get_graduates():
        print(student)

    student_id_to_find = input("Enter student ID to find their faculty: ")
    faculty_of_student = tum.find_student_faculty(student_id_to_find)
    if faculty_of_student:
        print(f"\nStudent {student_id_to_find} belongs to: {faculty_of_student.name}")
    else:
        print("Student not found.")

    print("\nAll Faculties:")
    tum.display_faculties()

    field_to_search = input("Enter a field to search for faculties: ")
    print("\nFaculties in {}:".format(field_to_search))
    tum.display_faculties_by_field(field_to_search)
