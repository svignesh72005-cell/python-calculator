def greet(name):
    return f"Hello, {name}!"

name = input("Enter your name: ")
print(greet(name))

print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

num = 5
while num > 0:
    print("Countdown:", num)
    num -= 1

