from bank import value

def test_greeting1():
	assert value("Hello sir have a nice day") == 0
	assert value("Hi sir how are u doing") == 20
	assert value("Adeiu Adeui sir!") == 100
	assert value("You are looking great sir") == 100
	assert value("Hello sir, hope u having a nice day") == 0
