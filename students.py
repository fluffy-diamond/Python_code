class Student:
    grade = 10
    subject = "coding"

    def __init__(self, name):
        self.name = name

    def details(self):
        return "My name is {} and I am in grade {} and I study {}".format(
            self.name, self.grade, self.subject
        )


heer = Student("Heer")
print(heer.details())