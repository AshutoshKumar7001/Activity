# guessing.game
import random

rand_num = random.randint(1, 101)
#Hint>:::::::::::::::
print("The random genetated number is : ", rand_num )
count =5
while count!=0:
    num = int(input("Guess any number between 1 to 100 to win the game : "))
    if(rand_num == num):
        print(":) Congratulations!! You Won !! :)")
        break
    else:
        count-=1
        print("Oops worng guess !! Try again!! [", count, "] Attemp left.")
        if (rand_num > num):
            print("Your guessed number is small !")
        elif(rand_num<num):
            print("Your guessed number is large !")

    if (count== 0):
        print("Better Luck Next time > :(")
    else:
        ans = input("Do You want to continue [y/n] : ")
        if(ans == "y"):
            continue
        else:
            print("Thanks for visiting :)")
            break
