f = open("output.txt", "a")

a = input("Enter text to write to the file: ")
f.write(a+"\n")

print("Data successfully written to output.txt")
print()

b = input("Enter additional text to append: ")
f.write(b+"\n")
print("Data successfully appended")
f.close()
print()

f = open("output.txt", "r")
print("Final content of output.txt")
for i in f.readlines():
    print(i[:-1])