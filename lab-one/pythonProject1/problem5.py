data=input("enter the data please \n")
vowels =['a','e', 'i' ,'o']
data_list=[]


for i in range(len(data)):
    data_list.append(data[i])
for i in range(len(data)):
    for z in range(4):
        if vowels[z] in data_list:
            data_list.remove(vowels[z])


for i in range(len(data_list)):
    if " " in data_list:
        data_list.remove(" ")



print(data_list)
