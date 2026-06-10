from twttr import shorten

def test_shorten():
    assert shorten("hi this is my twitter handle") == "h ths s my twttr hndl"
    assert shorten("i am feeling lucky") == " m flng lcky"
    assert shorten("clouds are amazing today") == "clds r mzng tdy"
    assert shorten("this is a wonderful day") == "ths s  wndrfl dy"
    assert shorten("storm my brain with ideas") == "strm my brn wth ds"