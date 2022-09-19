language = "English"
if language == "English":
    print("Hello")
print("End")

print("---")

language = "Russian"
if language == "English":
    print("Hello")
else:
    print("Привет")
print("End")

print("---")

language = "Russian"
if language == "English":
    print("Hello")
elif language == "Germany":
    print("Hi...")
else:
    print("Привет")
print("End")

print("---")

language = "russian"
daytime = "morning"
if language == "english":
    if daytime == "morning":
        print("Good morning")
    else:
        print("Good evening")
else:
    if daytime == "morning":
        print("Доброе утро")
    else:
        print("Добрый вечер")