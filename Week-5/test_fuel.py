from fuel import convert, gauge

def test_convert():
	assert convert(["0","4"]) == 0
	assert convert(["1","4"]) == 25
	assert convert(["2","4"]) == 50
	assert convert(["3","4"]) == 75
	assert convert(["4","4"]) == 100

def test_gauge():
	assert gauge(0.5) == "E"
	assert gauge(99.2) == "F"
	assert gauge(50) == "50%"