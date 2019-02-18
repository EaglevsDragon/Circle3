rest = int(input("Введіть кількість центів які повинен видати продавець "))
a = 0  # 25 центів
b = 0  # 10 центів
c = 0  # 5 центів
d = 0  # 1 цент
while rest > 0:
    if 0 < rest < 5:
        d = d + 1
        rest = rest - 1
        # print("1 цент", d)
    if 4 < rest < 10:
        c = c + 1
        rest = rest - 5
        # print("5 центів", c)
    if 9 < rest < 25:
        b = b + 1
        rest = rest - 10
        # print("10 центів", b)
    if rest > 24:
        a = a + 1
        rest = rest - 25
        # print("25 центів", a)
s = a + b + c + d
print("Продавцю необхідно натиснути на гачки видавача таку кількість разів - ", s)
#print(a, b, c, d)
