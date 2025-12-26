age = int(input("How old are you?\n"))
# input returns as string

decades = age // 10
years = age % 10

print("You are ", decades, " decades and ", years, " years old")