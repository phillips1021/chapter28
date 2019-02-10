import manager
import person


def test_give_raise():
    bruce = manager.Manager('Bruce', 'Programmer', 100)
    bruce.give_raise(.10)
    assert bruce.pay == 120


def test_give_raise_bonus():
    bruce = manager.Manager('Bruce', 'Programmer', 100)
    bruce.give_raise(.10, .20)
    assert bruce.pay == 130


def test_multiple_give_raise():
    bruce = manager.Manager('Bruce', 'Programmer', 100)
    sue = person.Person('Sue', 'Assistant', 100)
    for obj in (bruce, sue):
        obj.give_raise(.10)
    assert bruce.pay == 120
    assert sue.pay == 110
