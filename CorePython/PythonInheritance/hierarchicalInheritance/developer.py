from employee import Employee
class Developer(Employee):
    def __init__(self, emp_name, emp_id, programming_lang):
        Employee.__init__(self, emp_name, emp_id)
        self.programming_lang = programming_lang

    def show_developer_details(self):
        self.display_info()
        print(f"Programming Language : {self.programming_lang}")


developer = Developer(emp_name="Ram Pandey", emp_id=1, programming_lang="Python")
developer.show_developer_details()