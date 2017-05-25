# file = open("sample.txt", "w")
# file.write("Hello my name is Jake\nWhat's yours?")
# file.close()


with open("sample.txt", "w") as file:
    file.write("Hello my name is Jake\nWho are you?")
