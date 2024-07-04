class Employee:

    def __init__(self, first_name, last_name):
        self.__first_name = first_name  # Private attribute :  double underscore prefix __
        self.__last_name = last_name  # Private attribute

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def __employee_details(self):  # Private method
        print(f"Name : {self.__first_name} {self.__last_name}")

    def show_employee_info(self):
        self.__employee_details()  # Accessible within the class


emp = Employee("Ram", "Dahal")
emp.set_first_name("Sita")
emp.set_last_name("Rai")

emp.show_employee_info()
