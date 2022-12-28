import controller

def getChoise():
    return input("Нажмите <s> чтобы продолжить игру: ")

def viewMassage(mas):
    print(mas)

def getLoop():
    return mainloop

def mainloop():
    while True:
        controller.controller()