from calc import add, subtract, multiply, divide


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert subtract(2, 1) == 1


def test_mul():
    assert multiply(2, 1) == 2


def test_div():
    assert divide(6, 2) == 3