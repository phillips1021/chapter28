class Department:

    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, employee):
        self.members.append(employee)

    def give_raises(self, percent=0):
        for employee in self.members:
            employee.give_raise(percent)
