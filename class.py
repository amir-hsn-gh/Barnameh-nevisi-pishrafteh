class Student:
    def __init__(self, first_name, last_name, student_id, major):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.major = major
        self.courses = []

    def add_course(self, course_name, grade, units):
        course = {
            "name": course_name,
            "grade": grade,
            "units": units
        }
        self.courses.append(course)

    def calculate_gpa(self):
        if not self.courses:
            return 0
        total_points = sum(course["grade"] * course["units"] for course in self.courses)
        total_units = sum(course["units"] for course in self.courses)
        return round(total_points / total_units, 2)

    def is_probation(self):
        gpa = self.calculate_gpa()
        return gpa < 12

    def display_grades(self):
        if not self.courses:
            print("hich darsi sabt nashode ast.")
            return
        print("riz nomarat:")
        for course in self.courses:
            print(f"- {course['name']}: nomre {course['grade']}، vahed {course['units']}")

    def display_info(self):
        gpa = self.calculate_gpa()
        print(f"nam: {self.first_name}")
        print(f"name khanevadegi: {self.last_name}")
        print(f"shomare daneshjoyi: {self.student_id}")
        print(f"reshte tahsili: {self.major}")
        print(f"moadel: {gpa}")
        print(f"vaziyat: {'mashrot' if self.is_probation() else 'addi'}")


student1 = Student("amir hossein", "ghorbani", "02121040709025", "mohandesi control")

student1.add_course("riyazi mohandesi", 18, 2)
student1.add_course("barname nevisi pishrafte", 15, 2)
student1.add_course("filter va santez", 10, 2)

student1.display_info()
student1.display_grades()