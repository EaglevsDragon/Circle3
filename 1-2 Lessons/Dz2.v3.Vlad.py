from random import randint

print("Привіт, я б хотів зіграти з тобою в гру, як твоє імя?")
name = input()
ZagadaneChislo = randint(1, 20)
print(f"Гаразд, {name}, я загадав число від 1 до 20 і хочу щоб ти його відгадав, у тебе є 5 спроб")

ChisloPlayera = 0
tries = 0

while ChisloPlayera != ZagadaneChislo:
    ChisloPlayera = int(input("Введи число від 1 до 20 - "))
    tries = tries + 1
    if tries >= 5:
        print("Ти програв,пощастить наступного разу!")
        print(f"Я загадав число {ZagadaneChislo}.")
        break
    if ChisloPlayera > ZagadaneChislo:
        print(f"Я загадав менше число, залишилось {5 - tries} спроб")
    elif ChisloPlayera < ZagadaneChislo:
        print(f"Я загадав быльше число, залишилось {5 - tries} спроб")
    else:
        print(f"{name}, ти вгадав число,це {ZagadaneChislo}, тобі знадобилось {tries} спроб!")
        break
