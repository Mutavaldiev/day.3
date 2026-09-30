# test 1

# with open("text.txt", "w") as file:
#     file.write("salom, Jahon!")



# test 2


# with open("text.txt", "r") as file:
#     f = file.readline()
# print(f)




# test 3

# with open("hello.txt") as file:
#     for i in file:


# test 4



# with open("notes.txt", "r") as file:
#     lines = file.readlines()
#     count = len(lines)
#     print(len(lines))




# test 5




# with open("notes.txt", "a") as file:
#     file.write("orange\n")



# test 6



# names = ["Ali", "Vali", "Guli", ]

# with open("names.txt", "w") as file:
#     for i in names:
#         file.writelines(i + "\n" )




# test 7




# cnt = 0

# with open("text.txt", "r") as file:
#     for i in file:
#         words = i.split()
#         cnt += len(words)

# print(cnt)




# testt 8



# with open("text.txt", "r") as file:
#        text = file.read()

# count = text.replace(" ", "")
# print(count)


# Task 9

# with open("text.txt", "r") as file:
#     numbers = [int(line.strip()) for line in file]
# print(sum(numbers))


# Task 10

# with open("text.txt", "r") as file:
#     numbers = [int(line.strip()) for line in file]
# print(max(numbers))


# Task 11


# import shutil

# shutil.copy("text.txt", "copy.txt")


# Task 12

# with open("notes.txt", "r") as file:
#     for line_number, line in enumerate(file, start=1):
#         print(f"{line_number}: {line.strip()}")


# Task 13

# with open("text.txt", "r") as file:
#     words = file.read().split()
# print(words.count("python"))


# Task 14


# with open("text.txt", "r") as file:
#     longest_line = max(file, key=len).rstrip("\n")
# print(longest_line)


# Task 15

# with open("text.txt", "r") as file:
#     uppercase_text = file.read().upper()
#
# with open("upper.txt", "w") as file:
#     file.write(uppercase_text)


# Task 16

# with open("text.txt", "r") as file:
#     nonempty_lines = [line for line in file if line.strip()]
#
# with open("clean.txt", "w") as file:
#     file.writelines(nonempty_lines)


# Task 17

# with open("file1.txt", "r") as first_file:
#     lines = first_file.readlines()
#
# with open("file2.txt", "r") as second_file:
#     lines.extend(second_file.readlines())
#
# with open("merged.txt", "w") as merged_file:
#     merged_file.writelines(line.rstrip("\n") + "\n" for line in lines)


# Task 18

# scores = []
# with open("scores.txt", "r") as file:
#     for line in file:
#         name, score = line.split()
#         scores.append((name, int(score)))
#
# average_score = sum(score for _, score in scores) / len(scores)
# top_student = max(scores, key=lambda student: student[1])[0]
# print(f"Average: {average_score:.2f}")
# print(f"Top: {top_student}")


# Task 19

# counts = {}
# with open("text.txt", "r") as file:
#     for word in file.read().split():
#         counts[word] = counts.get(word, 0) + 1
#
# with open("freq.txt", "w") as file:
#     for word, count in counts.items():
#         file.write(f"{word}: {count}\n")


# Task 20

# class Contact:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
# contacts = []
# with open("contacts.txt", "r") as file:
#     for line in file:
#         name, phone = line.strip().split(",")
#         contacts.append(Contact(name, phone))
#
# contacts.append(Contact("Sara", "555-1234"))
#
# with open("contacts.txt", "w") as file:
#     for contact in contacts:
#         file.write(f"{contact.name},{contact.phone}\n")
#     file.readline()
# print(file)

