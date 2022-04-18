with open("/Users/ben/Desktop/data.txt", mode="w") as data:
    data.write("Hi my name is ben, does this work?")
with open("/Users/ben/Desktop/data.txt") as data:
    text = data.read()
print(f"{text}")

