from person import Person


class Manager(Person):

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)
