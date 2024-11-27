class Student:

    def __init__(self, first_name, last_name, course_type,
                 university):  # Constructor
        # self refers to the instance of the class
        self.first_name = first_name
        self.last_name = last_name
        self.course_type = course_type
        self.university = university

    def toDictionary(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "course_type": self.course_type,
            "university": self.university
        }
