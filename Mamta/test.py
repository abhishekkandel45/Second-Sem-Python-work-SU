import numpy as np
#Ask user the total size of array
n=int(input('Enter n:'))
#declaring 1D arrays
arx=[]
ary=[]

#user input array elements
for i in range (n):
    x=float(input('Enter x value: '))
    y=float(input('Enter y value: '))
    arx.append(x)
    ary.append(y)


#components needed for table and sum calculated
print("x \t\t\t y \t\t\t x^2\t\t x^3\t\t x^4\t\t x.y\t\t  x^2.y\t\t")
sumx=sumy=sumx2=sumx3=sumx4=sumxy=sumx2y=0
for i in range (n):
    x2= arx[i]*arx[i]
    x3=arx[i]**3
    x4=arx[i]**4
    x2y=(arx[i]**2)*ary[i]
    xy=arx[i]*ary[i]
    print("{:0.3f}\t\t {:0.3f}\t\t {:0.3f}\t\t {:0.3f}\t\t {:0.3f}\t\t {:0.3f}\t\t  {:0.3f}\t\t".format(arx[i],ary[i],x2,x3,x4,xy,x2y))
    
    
    sumx= sumx+arx[i]
    sumy=sumy+ary[i]
    sumx2=sumx2+x2
    sumx3=sumx3+x3
    sumx4=sumx4+x4
    sumxy=sumxy+xy
    sumx2y=sumx2y+x2y
    

print('\t')
print("sum x= {:0.3f}\t , sum y={:0.3f}\t, sum x^2={:0.3f}\t, sum x^3={:0.3f}\t, sum x^4={:0.3f}\t, sum x.y={:0.3f}\t,sum x^2.y={:0.3f}\t".format(sumx,sumy,sumx2,sumx3,sumx4,sumxy,sumx2y))

#Displaying the normal equations:
print('\t')
print('The normal equations are:')
print("{:0.3f}\t = ({:0.3f})*a\t+({:0.3f})*b\t+({:0.3f})*c\t".format(sumy,n,sumx,sumx2))
print("{:0.3f}\t = ({:0.3f})*a\t+({:0.3f})*b\t+({:0.3f})*c\t".format(sumxy,sumx,sumx2,sumx3))
print("{:0.3f}\t = ({:0.3f})*a\t+({:0.3f})*b\t+({:0.3f})*c\t".format(sumx2y,sumx2,sumx3,sumx4))

#solving the normal equations
A=np.array([(n,sumx,sumx2),(sumx,sumx2,sumx3),(sumx2,sumx3,sumx4)])
B=np.array([(sumy),(sumxy),(sumx2y)])
X=np.dot(np.linalg.inv(A),B)
print('\t')
#displaying final equation
print('The required equation is: ')
print('y= ({:0.2f})\t+ ({:0.2f})*x\t+ ({:0.2f})*x^2\t'.format(X[0],X[1],X[2]) )