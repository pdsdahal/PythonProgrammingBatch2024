from abstract_class import Student


class Course(Student):

    def set_student(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def get_student(self):
        return "Name : " + self.name + "\nAddress : " + self.address + "\nAge : " + str(self.age)


course = Course()
course.set_student("Ram Pandey", "St.Louis", 13)
print(course.get_student())
