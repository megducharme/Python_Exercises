class Department(object):
    """Parent class for all departments"""

    def __init__(self, name):
        self.employees = set()
        self.__name = name

    @property
    def name(self):
        try:
            return self.__name
        except AttributeError:
            return ""

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise TypeError('Please provide a string value for the department name')

        if val is not "" and len(val) > 1:
            self.__name = val
        else:
            raise ValueError("Please provide a department name")

    @property
    def supervisor(self):

        try:
            return self.__supervisor
        except AttributeError:
            return ""

    @supervisor.setter
    def supervisor(self, val):
        if not isinstance(val, str):
            raise TypeError('Please provide a string value for the supervisor name')

        if val is not "" and len(val) > 5:
            self.__supervisor = val
        else:
            raise ValueError("Please provide a supervisor name")


hr = Department("Human Resources")
hr.name = "Human Resourcez"
hr.supervisor = "Meg Ducharme"
print(hr.name)
print(hr.supervisor)

