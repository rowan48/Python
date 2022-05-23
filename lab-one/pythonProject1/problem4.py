if __name__ == '__main__':
    afile=input("enter the name of the file  please : \n")
    afile=afile+".txt"
    my_list=[]
    f = open(afile)
    data=f.read()
    print(data)
    my_list=data.split()
    print(my_list)
    res=[]
    print(type(len(my_list)))
    for i in range (len(my_list)):
        output= my_list.count(my_list[i])
        if(int(output)>=20):
            if my_list[i] not in res:
                res.append(my_list[i])




    # Python program to convert a list to string

    # Function to convert
    def listToString(s):

        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 += ele+"\n"

            # return string
        return str1
    words=listToString(res)

    f = open("popular_words.txt", "w")
    f.write(words)
    f.close()


