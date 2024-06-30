class University:
    # constructor
    def __init__(self, uni_name, uni_address):
        self.uni_name = uni_name
        self.uni_address = uni_address

    def show_uni_details(self):
        print(f"University Name : {self.uni_name}\nUniversity Addess : {self.uni_address}")
