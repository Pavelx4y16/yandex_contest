from tasks.task2.main import main_algo


def test_standard():
    actual = main_algo(4, [1, 2, 3, 4])
    expected = 5000
    assert actual == expected

    actual = main_algo(5, [5, 5, 5, 5, 5])
    expected = 2_500
    assert actual == expected

    actual = main_algo(4, [4, 2, 3, 3])
    expected = 3000
    assert actual == expected


def test_reverse_order():
    actual = main_algo(8, [8, 7, 6, 5, 4, 3, 2, 1])
    expected = 18_000
    assert actual == expected

    actual = main_algo(4, [4, 3, 2, 1])
    expected = 5_000
    assert actual == expected


def test_special_case():
    actual = main_algo(6, [1, 2, 1, 2, 1, 2])
    expected = 4_500
    assert actual == expected

    actual = main_algo(4, [1, 1, 2, 2])
    expected = 2_500
    assert actual == expected

    actual = main_algo(1, [0])
    expected = 500
    assert actual == expected

    actual = main_algo(7, [2, 3, 4, 4, 3, 2, 1])
    expected = 8000
    assert actual == expected

    actual = main_algo(2, [2, 1])
    expected = 1_500
    assert actual == expected

    actual = main_algo(11, [1, 1, 2, 3, 4, 3, 2, 4, 3, 4, 4])
    expected = 10_500
    assert actual == expected

    actual = main_algo(3, [1, 2, 1])
    expected = 2000
    assert actual == expected
