from employee import Employee


class Manager(Employee):
    def __init__(self, emp_name, emp_id, man_dep):
        Employee.__init__(self, emp_name, emp_id)
        self.man_dep = man_dep

    def show_manager_details(self):
        self.display_info()
        print(f"Department : {self.man_dep}")


manager = Manager(emp_name="Ram Pandey",emp_id=1, man_dep="Computer")
manager.show_manager_details()
