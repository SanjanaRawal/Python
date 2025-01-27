f = open("11_text", "w")
line = []
for i in range(0, 9):
    line.append(("line", i + 1))
print(line)

for i in line:
    f.write(f"{i[0]} {i[1]}\n")  # Write each tuple's elements as a string
f.close()

f = open("11_text", "r")
print("File opened successfully and it contains:")
print(f.read())
f.close()
print("File closed")