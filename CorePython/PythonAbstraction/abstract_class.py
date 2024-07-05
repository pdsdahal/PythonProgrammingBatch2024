from abc import ABC, abstractmethod


class Student(ABC):
    @abstractmethod
    def set_student(self, name, address, age):
        pass

    @abstractmethod
    def get_student(self):
        pass
