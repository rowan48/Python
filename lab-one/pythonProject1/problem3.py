if __name__ == '__main__':
    my_str=input("enter a string : ")
    front=[]
    back=[]
    if(len(my_str)%2 ==0):
        for i in range(len(my_str)):
            front=my_str[:int((len(my_str)/2))]
            back=my_str[int((len(my_str)/2)):]
    else:
        for i in range(len(my_str)):
            front = my_str[:(int((len(my_str) / 2))+1)]
            back = my_str[(int((len(my_str) / 2))+1):]
    print(front)
    print(back)
    front_str=str(front)+"-front"+" "+str(back)+"-front"
    back_str=str(front)+"-back"+" "+str(back)+"-back"
    print(front_str)
    print(back_str)
