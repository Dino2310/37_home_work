from it_man import it_men


num = int(input("Введите количесвто языков программирования, которые знает Вася - первый программист: "))
vasya = it_men(num)
vasya.input_lang()
print("Ok" if len(vasya) else "Недостаточно")


num = int(input("Введите количесвто языков программирования, которые знает Петя - второй программист: "))
petya = it_men(num)
petya.input_lang()
print("Ok" if len(petya) else "Недостаточно")


if vasya + petya:
    print("Программист Вася знает больше языков")
elif petya + vasya:
    print("Программист Петя знает больше языков")
else:
    print("У обих программистов знания одинаковые")