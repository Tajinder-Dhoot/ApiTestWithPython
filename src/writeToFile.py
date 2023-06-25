
def print_line_in_file():
    with open('../files/text.txt') as file:
        content = file.readlines() # store lines as list
        for line in content:
            print(line)


def write_to_file():
    with open('../files/text.txt', 'r') as reader:
        content = reader.readlines()
        for line in content:
            with open('../files/text.txt', 'w') as writer:
                writer.write(line)


print_line_in_file()
write_to_file()
print_line_in_file()
