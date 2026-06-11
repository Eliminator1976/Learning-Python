def main():
	greeting = input("What was the greeting? ")
	print(value(greeting))

def value(greeting):
	if "".join(greeting.lower().split(sep=" ")[0:1]) == "hello":
		return 0
	elif "".join(list(greeting.lower()[0:1])) == "h":
		return 20
	else:
		return 100


if __name__ == "__main__":
	main()