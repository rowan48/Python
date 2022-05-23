data, charachter = input("Enter the string and the charachter: ").split()
data_list=[]
count=0
inds=[]
for i in range(len(data)):
    data_list.append(data[i])
for i in range(len(data_list)):
    if data_list[i]==charachter:
        #print(data_list[i])
        print(charachter)
        count+=1
        inds.append(i+1)
print(f"number of repeted charachter is {count} and it's index's are {inds} ")