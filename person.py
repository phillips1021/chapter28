class Person:
    """
    Models a Person
    """

    company_name = "Cboe"

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        """
        Increases pay by percent.
        :param percent: decimal value like .10
        :return: void
        """
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s %s %s %s]' % (Person.company_name, self.name, self.job, self.pay)
