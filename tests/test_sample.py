from sklatent import (
    add as sk_add,
    main,
)


def test_main():
    assert main() is None


def test_add():
    assert sk_add(1, 2) == 3
    assert sk_add(-1, 1) == 0
    assert sk_add(-1, -1) == -2
