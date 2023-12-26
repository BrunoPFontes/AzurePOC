# This is a sample Python script.
import random
import string


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    # a = int(input("w: "))
    # b = float(input("h: "))
    # c = float(input("tip: 10, 12, 15 "))
    # total = None

    # a = 5
    # b = 100
    #
    # c = a = 5
    # a = b = 100
    # b = c = 5

    #
    # c = a
    # a = b
    # b = c
    # total = round(float(a / b ** 2))

    # if total <= 18.5:
    #     message = "Under"
    # elif total <= 25.0:
    #     message = "Normal"
    # elif total <= 30.0:
    #     message = "Over"
    # else:
    #     message = "clinically"
    # print(f"This is your - {total} and you are {message}")
    # print("b: " + b)
    # print("c: " + c)

    ##################################################################
    # message = False
    # if a % 4 != 0:
    #     message
    # elif a % 400 == 0:
    #     message = True
    # elif a % 100 == 0:
    #     message = False
    # else:
    #     message = True

    ##################################################################
    # a = input("s: ")
    # b = input("p: ")
    # c = input("c: ")
    # t = 0
    # if a == "l":
    #     t = 25
    #     if b == "y":
    #         t += 3
    #     if c == "y":
    #         t += 1
    # elif a == "m":
    #     t = 20
    #     if b == "y":
    #         t += 3
    #     if c == "y":
    #         t += 1
    # elif a == "s":
    #     t = 15
    #     if b == "y":
    #         t += 2
    #     if c == "y":
    #         t += 1
    # else: t = "Error"
    #
    # print(f"This is your {t}")

    ##################################################################
    # and or not

    # a = int(input("w: "))
    # b = float(input("h: "))
    # c = float(input("tip: 10, 12, 15 "))
    # total = None
    #
    # a = input("a: ").lower()
    # b = input("b: ").lower()
    # t = 0
    # v = 0
    #
    # l = ["t","r","u","e","l","o","v","e"]
    # # l = ["truelove"]
    #
    # for x in a:
    #     # print(a)
    #     # print(x)
    #     if x in l:
    #         t += 1
    #
    # for y in b:
    #     if y in l:
    #         v += 1
    #
    # print("This is your " + str(t) + str(v))

    ##################################################################
    #
    # a = int(input("0, 1 or 2 "))
    # b = random.randint(0, 2)
    # #<editor-fold desc="Rock, scissor, paper">
    # # rock, scissor, paper
    # # 0 = rock
    # # 1 = scissor
    # # 2 = paper
    # print(b)
    #
    # if a == b:
    #     print("Draw")
    # elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
    #     print("Won")
    # elif (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
    #     print("Lost")
    # else:
    #     print("Wrong value")

    ##################################################################

    # a = random.randint(0, 100)
    # print(f" a's value is {a} ")

    ##################################################################
    # bill = input("Print a bunch of people name separated by a comma ")
    #
    # print (f"{bill.split(',')[random.randint(0, len(bill.split(','))-1)]} will pay the bill ")

    ##################################################################

    # av =""
    # bv =""
    # cv =""
    # a = input("How many letters would like in your password? ")
    # for y in range(int(a)):
    #     av += random.choice(string.ascii_letters)
    # b = input("How many symbols would like in your password? ")
    # for y in range(int(b)):
    #     bv += random.choice(string.digits)
    # c = input("How many numbers would like in your password? ")
    # for y in range(int(c)):
    #     cv += random.choice(string.punctuation)
    #
    #
    # pswrd = av+bv+cv
    # pswrd = list(pswrd)
    #
    # pswrd_shuffled = ''.join(random.sample(pswrd,(len(pswrd))))
    # # pswrd_shuffled = ''.join(random.shuffle(pswrd))
    #
    # print(f"Here is your password {pswrd_shuffled } ")

    ##################################################################

    # height = input("Provide a list of students height").split(',')
    # # height = float(height)
    # total = 0.0
    # for each in height:
    #    total += (float(each)/len(height))
    #
    # print(round(total, 0))

    ##################################################################

    height = input("Provide the grades").split(',')
    # height = float(height)
    total = 0
    for each in height:
        if int(each) > int(total):
            total = each

    print(total)


# PEMDAS

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
