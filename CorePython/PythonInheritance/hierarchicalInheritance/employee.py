class Employee:
    def __init__(self, emp_name, emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Name : {self.emp_name}\nId = {self.emp_id}")
