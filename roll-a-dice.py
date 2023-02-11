import random
responce = input("do you want to roll the dice or not")
responce="y"
def dice(responce):
    while responce == "y":
        ran = random.randint(1,6)
        if(ran==1):
            print("---")
            print("-*-")
            print("---")
        elif(ran==2):
            print("--*")
            print("---")
            print("*--")
        elif(ran==3):
            print("--*")
            print("-*-")
            print("*--")
        elif(ran==4):
            print("*-*")
            print("---")
            print("*-*")
        elif(ran==5):
            print("*-*")
            print("-*-")
            print("*-*")
        elif(ran==6):
            print("*-*")
            print("*-*")
            print("*-*")
        responce = input("type y if you want  to roll again or n if ou want to stop")
        if(responce=="n"):
            quit()
dice(responce)
