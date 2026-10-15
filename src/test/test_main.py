import src.python.main as Main

import pytest


def test_main():
    result = Main.main()
    assert result == True

def test_main_2():
    result = Main.main()
    assert result != False

