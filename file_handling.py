filename = "data.txt"

text = input("intern name : ")
with open(filename, "w") as file:
    file.write(text)

print("Data written to file.")


with open(filename, "r") as file:
    content = file.read()

print("File content:")
print(content)

