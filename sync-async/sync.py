def read_file():
	print("Before read")
	with open("sample.txt", "r") as file:
		data = file.read()
		print(data)
	print("After read")
	


if __name__ == "__main__":
	read_file()