from one_hot_encoder import fit_transform
import pytest


def test_equal():
    transformed = fit_transform('hello', 'Amal')
    expected = [
        ('hello', [0, 1]),
        ('Amal', [1, 0])
    ]
    assert transformed == expected


def test_empty():
    with pytest.raises(TypeError):
        fit_transform()


def test_doubles():
    transformed = fit_transform('hello', 'Amal', 'hello')
    expected = [
        ('hello', [0, 1]),
        ('Amal', [1, 0]),
        ('hello', [0, 1]),
    ]

    assert transformed == expected


def test_one_el():
    actual = fit_transform('Amal')
    expected = [('Amal', [1])]
    assert actual == expected
