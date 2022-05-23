# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
 x1=int(input("enter the x1"))
 x2=int(input("enter x2"))
 while(x2<x1):
  x2 = int(input("enter x2 to be greater than x1"))

 y1=int(input("enter y1"))
 y2=int(input("enter y2"))
 while(y2<y1):
  y2 = int(input("enter y2 to be greater than y1"))
 x=x2-x1
 y=y2-y1
 xsq=pow(x,2)
 ysq=pow(y,2)
 value=xsq=ysq
 d=pow(value,0.5)
 print("the output is: ",d)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
