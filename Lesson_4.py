# Циклы
# frutic = ["яблоко", "груша", "виноград"]
# for frut_1 in frutic:
#     print(frut_1)
# message = "Hello World"
# for letter in message:
#     print(letter.upper())
# homan = {
#     "name": "ALEX",
#     "age": 42,
#     "city": "Stavropol"
# }
# for key, value in homan.items():
#     print(f"{key}: {value}")
# print(list(range(1,10)))
# count = 0
# while count < 10:
#     print(f"Счетчик = {count}")
#     count += 1
while True:
    answer = input("Хотите продолжить? да/нет")
    if answer == "нет":
        break
    elif answer == "да":
        continue
    else:
        print("Читай внимательнее")
