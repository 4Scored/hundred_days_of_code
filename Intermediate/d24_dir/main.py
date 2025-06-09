# indirect progress
# - changes made to snake game (d20-d21)
#      - high score functionality added
# - this file, file open/close, rwx demonstration

# ----------------------------

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt", mode="a") as file: # using "with" - no need to close files
    file.write("\nhello world")

    # mode="a" append
    # mode="r" read
    # mode="w" write