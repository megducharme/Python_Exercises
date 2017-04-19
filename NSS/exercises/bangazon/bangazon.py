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


class HumanResources(Department):
    """Class for representing Human Resources department

    Methods: __init__, add_policy, get_policy, etc.
    """

    def __init__(self, name, supervisor, employee_count):
        super().__init__(name, supervisor, employee_count)
        self.policies = set()

    def add_policy(self, policy_name, policy_text):
        """Adds a policy, as a tuple, to the set of policies

        Arguments:
        policy_name (string)
        policy_text (string)
        """

        self.policies.add((policy_name, policy_text))

    def __str__(self):
        return "The {} department is supervised by {} and has {} employees".format(self.name, self.supervisor, self.employee_count)


hr = HumanResources("HR", "Toby Flenderson", 3)
print(hr)


