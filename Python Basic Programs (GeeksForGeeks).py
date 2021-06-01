#!/usr/bin/env python
# coding: utf-8

# In[1]:


#add two numbers
a=int(input())
b=int(input())
sum=a+b
print(sum)


# In[1]:


#max of two numbers
a=int(input())
b=int(input())
max = a if a > b else b
print(max)


# In[3]:


#factorial of a number
n=int(input())
factorial=1
if n<0:
    print("Invalid")
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)


# In[5]:


#simple interest = prt/100
si=0
principle=int(input())
rate=int(input())
time=int(input())
si=(principle*rate*time)/100
print(int(si))


# In[8]:


#compound Interest => A = P(1 + r/n)^nt
#A	=	final amount
#P	=	initial principal balance
#r	=	interest rate
#n	=	number of times interest applied per time period
#t	=	number of time periods elapsed
A=0
CI=0
P=int(input())
r=int(input())
t=int(input())
A=P*(pow((1+r/100),t))
CI=A-P
print(int(CI))


# In[13]:


#armnstrong number 153 = 1*1*1 + 5*5*5 + 3*3*3
num=int(input())
sum=0
while num > 0:
    digit=num%10
    sum = digit ** 3
    num//=10
if num == sum:
    print("Armstrong")
else:
    print("Not Armstrong")


# In[18]:


#area of circle
r=int(input())
area=3.14*(r**2)
print(area)


# In[22]:


#prime numbers in an interval
start=int(input())
end=int(input())
for i in range(start, end+1):
    if i>1:
        for j in range(2,i):
            if(i % j==0):
                break
        else:
            print(i)


# In[29]:


#number is prime or not:
n=int(input())
if n>1:
    for i in range(2,int(n/2)+1):
        if (n%i)==0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")


# In[1]:


#nth fibonacci number
def fib(n):
    if n<0:
        print("invalid input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=int(input())
print(fib(n))


# In[33]:


#is number fibonacci ?
n=int(input())
c=0
a=1
b=1
if n==0 or n==1:
    print("yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("yes")
    else:
        print("no")


# In[34]:


#ascii value of charecter
c=input()
print(ord(c))


# In[38]:


#sum of square of n natural numbers
n=int(input())
print(int(n*(n+1)*(2*n+1)/6))


# In[40]:


#sum of cube of n natural numbers
n=int(input())
print(int(n*(n+1)/2)**2)


# In[ ]:




