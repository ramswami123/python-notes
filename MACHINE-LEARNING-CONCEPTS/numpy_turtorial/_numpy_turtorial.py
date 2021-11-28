import numpy as np
from numpy.core.fromnumeric import std
l=[2,6,0,8,5,6,9,4]
#creating array a using numpy
a=np.array(l);
  
#to know dimension of array
print(a.shape)
#output (4,)->reprensts dimensions of array

#using reshape we can change the dimensions of data
a=a.reshape(2,2,2)
print(a)

l1=[2,5,7]
l2=[7,6,0]
l3=[8,4,5]
b=np.array([l1,l2,l3])
#silicing using numpy
print(b[1:,1:])
#output [[6 0][4 5]]

#arange inbulit function
#->basically arrange inbulit function creates
#one dimensional array creates

#using 2 parameters
c=np.arange(0,10)
print(c)
#output [0 1 2 3 4 5 6 7 8 9]

#using 3 parameters
d=np.arange(1,10,step=1.5)
print(d)
#output [1.  2.5 4.  5.5 7.  8.5]
d=d.reshape(2,3)
print(d)
#[[1.  2.5 4. ]
#[5.5 7.  8.5]]

#linespace inbulit function
#this function is used create 1 array
#containg n elements by taking n as one of the parameter
e=np.linspace(1,5,20)#creates 20 elements between 1 and 5
print(e)
#ouput
#[1.         1.21052632 1.42105263 1.63157895 1.84210526 2.05263158       
#2.26315789 2.47368421 2.68421053 2.89473684 3.10526316 3.31578947       
#3.52631579 3.73684211 3.94736842 4.15789474 4.36842105 4.57894737       
#4.78947368 5.        ]

##some conditions useful foer explanatory data analysis
f=np.array([76,45,3,23,78,90,5,4,9,2,1,59])
print(f<2)
#output:[False False False False False False False False False False  True False]
print(f[f>10])
#output [76 45 23 78 90 59]
print(f/2)
#output [38.  22.5  1.5 11.5 39.  45.   2.5  2.   4.5  1.   0.5 29.5]
print(f*3)
#output [228 135   9  69 234 270  15  12  27   6   3 177]

#ones function
#here one function returns array of ones
# in desired dimentions
g=np.ones((3,3),dtype=float)
print(g)
#[[1. 1. 1.]
#[1. 1. 1.]
#[1. 1. 1.]]

#rand fuction
#this an array of return random normal distrubuted 
#values between [1,0]
h=np.random.rand(3,3)#3,3 is dimension of array
print(h)
#[[0.16525663 0.47968297 0.30750767]
#[0.90333871 0.46812622 0.21623863]
#[0.88529109 0.20084794 0.967054  ]]

#randn function
#this an array of return random uniformly distrubuted 
#values between [1,0]
i=np.random.randn(2,2)#(4,4) is dimension
print(i)
#output
#[[-0.01218163  1.70748848]
#[-0.32980371 -0.69823822]]
