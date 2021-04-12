import random

def common_div(a):
    div_a=[]
    for i in range(1,a+1):
        if a%i == 0:
            div_a.append(i)
    return div_a


def gcd(a,b):
    cd_a=common_div(a)
    cd_b=common_div(b)
    gcd=[]
    for i in cd_a:
        if i in cd_b:
            gcd.append(i)
    return gcd[-1]

num1=int(input("The first number for the greatest common divisor: "))
num2=int(input("The second number for the greatest common divisor: "))


print(f"The greatest common divisor of {num1} and {num2} is {gcd(num1,num2)}.")