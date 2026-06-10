from twttr import shorten

def test_shorten():
    assert shorten("hi this is my twitter handle") == "h ths s my twttr hndl"
    assert shorten("i am feeling lucky") == " m flng lcky"