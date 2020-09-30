from pprint import pprint
import pytest
import vyDebug
from vyDebug import VyDebugLevel, VyDebug
noPrint = vyDebug.vyDebug.noPrint # vyDebug.vyDebug.noPrint == package.module.function

def test_vyDebug_set_level_minus2():
    vyd = VyDebug()
    vyd.level = -2
    assert vyd.level == -1
    assert vyd.print0 == noPrint
    assert vyd.print1 == noPrint
    assert vyd.print2 == noPrint
    assert vyd.print3 == noPrint
    assert vyd.print4 == noPrint
    assert vyd.print5 == noPrint

def test_vyDebug_set_level_minus1():
    vyd = VyDebug()
    vyd.level = -1
    assert vyd.level == -1
    assert vyd.print0 == noPrint
    assert vyd.print1 == noPrint
    assert vyd.print2 == noPrint
    assert vyd.print3 == noPrint
    assert vyd.print4 == noPrint
    assert vyd.print5 == noPrint

def test_vyDebug_set_level_0():
    vyd = VyDebug()
    vyd.level = 0
    assert vyd.level == 0
    assert vyd.print0 == pprint
    assert vyd.print1 == noPrint
    assert vyd.print2 == noPrint
    assert vyd.print3 == noPrint
    assert vyd.print4 == noPrint
    assert vyd.print5 == noPrint

def test_vyDebug_set_level_1():
    vyd = VyDebug()
    vyd.level = 1
    assert vyd.level == 1
    assert vyd.print0 == pprint
    assert vyd.print1 == pprint
    assert vyd.print2 == noPrint
    assert vyd.print3 == noPrint
    assert vyd.print4 == noPrint
    assert vyd.print5 == noPrint

def test_vyDebug_set_level_2():
    vyd = VyDebug()
    vyd.level = 2
    assert vyd.level == 2
    assert vyd.print0 == pprint
    assert vyd.print1 == pprint
    assert vyd.print2 == pprint
    assert vyd.print3 == noPrint
    assert vyd.print4 == noPrint
    assert vyd.print5 == noPrint

def test_vyDebug_set_level_3():
    vyd = VyDebug()
    vyd.level = 3
    assert vyd.level == 3
    assert vyd.print0 == pprint
    assert vyd.print1 == pprint
    assert vyd.print2 == pprint
    assert vyd.print3 == pprint
    assert vyd.print4 == noPrint
    assert vyd.print5 == noPrint

def test_vyDebug_set_level_4():
    vyd = VyDebug()
    vyd.level = 4
    assert vyd.level == 4
    assert vyd.print0 == pprint
    assert vyd.print1 == pprint
    assert vyd.print2 == pprint
    assert vyd.print3 == pprint
    assert vyd.print4 == pprint
    assert vyd.print5 == noPrint

def test_vyDebug_set_level_5():
    vyd = VyDebug()
    vyd.level = 5
    assert vyd.level == 5
    assert vyd.print0 == pprint
    assert vyd.print1 == pprint
    assert vyd.print2 == pprint
    assert vyd.print3 == pprint
    assert vyd.print4 == pprint
    assert vyd.print5 == pprint

def test_vyDebug_set_level_6():
    vyd = VyDebug()
    vyd.level = 6
    assert vyd.level == 5
    assert vyd.print0 == pprint
    assert vyd.print1 == pprint
    assert vyd.print2 == pprint
    assert vyd.print3 == pprint
    assert vyd.print4 == pprint
    assert vyd.print5 == pprint

def test_vyDebug_set_prints_level_minus2():
    vyd = VyDebug(-2)
    assert vyd.level == -1
    assert vyd.print0 == noPrint
    assert vyd.print1 == noPrint
    assert vyd.print2 == noPrint
    assert vyd.print3 == noPrint
    assert vyd.print4 == noPrint
    assert vyd.print5 == noPrint

def test_vyDebug_set_prints_level_minus1():
    vyd = VyDebug(-1)
    assert vyd.print0 == noPrint
    assert vyd.print1 == noPrint
    assert vyd.print2 == noPrint
    assert vyd.print3 == noPrint
    assert vyd.print4 == noPrint
    assert vyd.print5 == noPrint

def test_vyDebug_set_prints_level_0():
    vyd = VyDebug(0)
    assert vyd.print0 == pprint
    assert vyd.print1 == noPrint
    assert vyd.print2 == noPrint
    assert vyd.print3 == noPrint
    assert vyd.print4 == noPrint
    assert vyd.print5 == noPrint

def test_vyDebug_set_prints_level_1():
    vyd = VyDebug(1)
    assert vyd.print0 == pprint
    assert vyd.print1 == pprint
    assert vyd.print2 == noPrint
    assert vyd.print3 == noPrint
    assert vyd.print4 == noPrint
    assert vyd.print5 == noPrint

def test_vyDebug_set_prints_level_2():
    vyd = VyDebug(2)
    assert vyd.print0 == pprint
    assert vyd.print1 == pprint
    assert vyd.print2 == pprint
    assert vyd.print3 == noPrint
    assert vyd.print4 == noPrint
    assert vyd.print5 == noPrint

def test_vyDebug_set_prints_level_3():
    vyd = VyDebug(3)
    assert vyd.print0 == pprint
    assert vyd.print1 == pprint
    assert vyd.print2 == pprint
    assert vyd.print3 == pprint
    assert vyd.print4 == noPrint
    assert vyd.print5 == noPrint

def test_vyDebug_set_prints_level_4():
    vyd = VyDebug(4)
    assert vyd.print0 == pprint
    assert vyd.print1 == pprint
    assert vyd.print2 == pprint
    assert vyd.print3 == pprint
    assert vyd.print4 == pprint
    assert vyd.print5 == noPrint

def test_vyDebug_set_prints_level_5():
    vyd = VyDebug(5)
    assert vyd.print0 == pprint
    assert vyd.print1 == pprint
    assert vyd.print2 == pprint
    assert vyd.print3 == pprint
    assert vyd.print4 == pprint
    assert vyd.print5 == pprint

def test_vyDebug_set_prints_level_6():
    vyd = VyDebug(6)
    assert vyd.print0 == pprint
    assert vyd.print1 == pprint
    assert vyd.print2 == pprint
    assert vyd.print3 == pprint
    assert vyd.print4 == pprint
    assert vyd.print5 == pprint

if __name__ == '__main__':
    pytest.main([__file__])
