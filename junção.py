"""""
print("Enter as many lines of text as you want.")
print("When you're done, enter a single period on a line by itself.")

buffer = []
while True:
    print("> ", end="")
    line = input()
    if line == ".":
        break
    buffer.append(line)
multiline_string = "\n".join(buffer)

print("You entered...")
print()
print(multiline_string)

"""

linha = " "
while True:
    print("> ", end="")
    line = input()
    if line == ".":
        break
    linha += line

print(linha)
