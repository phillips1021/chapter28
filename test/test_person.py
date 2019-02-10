import person


def test_person_contructor():
    bruce = person.Person('Bruce', 'Programmer', 125000)
    assert bruce.name == 'Bruce'


def test_person_constructor_defaults():
    bruce = person.Person('Bruce')
    assert bruce.job is None
    assert bruce.pay == 0


def test_last_name():
    bruce = person.Person('Bruce Phillips', 'Programmer', 125000)
    assert bruce.last_name() == 'Phillips'


def test_last_name_missing():
    bruce = person.Person('Bruce', 'Programmer', 125000)
    assert bruce.last_name() == 'Bruce'


def test_give_raise():
    bruce = person.Person('Bruce', 'Programmer', 100)
    bruce.give_raise(.10)
    assert bruce.pay == 110
