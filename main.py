# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

x= int(input("enter the number: "))
t1 =0
t2 =1
sum =0
total_sum =0
if x==0:
    print(t1)
elif x==1:
    t2 =1
    print(t2)




for i in range(2,x+2):
    sum = t1+t2
    t2 = t1
    t1 = sum

print(sum)