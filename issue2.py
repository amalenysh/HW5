from morse import decode
import pytest


@pytest.mark.parametrize('morse_str, result',
                         [
                             ('... --- ...', 'SOS'),
                             ('.... . .-.. .-.. ---', 'HELLO'),
                             (".-- --- .-. .-.. -..", 'WORLD')
                         ])
def test_decode(morse_str, result):
    assert decode(morse_str) == result
