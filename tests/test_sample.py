from sklatent import main
from sklatent.test_funcs import add as sk_add


def test_main():
    assert main() is None


def test_add():
    assert sk_add(1, 2) == 3
    assert sk_add(-1, 1) == 0
    assert sk_add(-1, -1) == -2
