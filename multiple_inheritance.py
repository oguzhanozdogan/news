class User:
    def __init__(self, soc_sec_nr):
        self.soc_sec_nr = soc_sec_nr

    
    def log_in(self):
        print("Logging in")


class Admin:
    def __init__(self, delete_permission):
        self.delete_permission = delete_permission


    def remove_student(self):
        if self.delete_permission == True:
            print("deleting student from list")
#Multiple inheritance
class Teacher(User, Admin):
    def __init__(self, soc_sec_nr, salary, delete_permission):
        User.__init__(self, soc_sec_nr)
        Admin.__init__(self, delete_permission)
        self.salary = salary

    
teacher_1 = Teacher("919394", 50000, True) 