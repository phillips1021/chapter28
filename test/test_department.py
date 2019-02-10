import department
import manager
import person


def test_department_constructor():
    bruce = manager.Manager('Bruce', 'Programmer', 100)
    sue = person.Person('Sue', 'Assistant', 100)
    accounting = department.Department(bruce, sue)
    assert len(accounting.members) == 2


def test_department_give_raises():
    bruce = manager.Manager('Bruce', 'Programmer', 100)
    sue = person.Person('Sue', 'Assistant', 100)
    accounting = department.Department(bruce, sue)
    accounting.give_raises(.10)
    assert bruce.pay == 120
    assert sue.pay == 110
