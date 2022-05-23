import random


my_data=random.randint(0, 100)
count=0
my_list=[]
play_again=True
not_finished=True
#print(my_data)
while(play_again and not_finished):
    for i in range (10):
        count=i
        user_input=int(input("guess the number:"))
        if user_input in my_list:
            print("u entered this no before")
            user_input = int(input("guess the number:"))
            my_list.append(user_input)
            i-=1
            count-=1
        else:
            my_list.append(user_input)
            count = i
            if(user_input==my_data):
                print("congratulations u did it")
                not_finished=False
                break
            elif(user_input>100):
                print("u cannot enter a no greater than 100")
                i -= 1
                count -= 1
            else:
                if(user_input>my_data):
                    print("enter a smaller no")
                else:
                    print("enter a larger no")


    if(count==9):
        again=input("ti you want to play again enter y")
        if(again!='y'):
            play_again=False
