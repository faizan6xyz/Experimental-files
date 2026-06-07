import numpy as np
import sys 
A = np.array([
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9],
    [10, 11, 12]
])
a = np.array([1, 2, 3, 4])
mask = np.array([True, False, True, False])
b = np.array([5, 6, 7, 8])
c = np.concatenate((a, b))
x = np.arange(5)  
y = np.arange(0, 10)  
z = np.arange(5, 0, -1) 
# size is optional , it will work without size also ans same 
dd = np.random.random(size=5)
aa = np.random.normal(size=5)
ss = np.random.rand(2, 4)
sa = np.linspace(0, 1, 5)
sq = np.random.rand(4)
ds = np.random.randn(3, 4)
print("random values :" , dd)
print("random numbers from normal distribution  :" , aa)
print("2d array of random values :" , ss)
print("linspace values :" , sa)
print("1d array of random values :" , sq)
print("2d array of random values from standard normal distribution :" , ds)
print ("Array x:", x)
print ("Array y:", y)
print ("Array z:", z)
print(sys.getsizeof(a))
print("boolean indexing of the array a : ", a[mask])
print("Array a:", a)
print("Array b:", b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("power : " ,a**b)
print("sum of a :",a.sum())
print("mean of a :" ,a.mean())
print("standard deviation :",a.std())
print("max of a :" ,a.max())
print("min of a :" ,a.min())
print("sum of b :",b.sum())
print("mean of b :" ,b.mean())
print("standard deviation :",b.std())
print("max of b :" ,b.max())
print("min of b :" ,b.min())
print("slicinf of a : ",a[1:-1:1])
print("slicinf of b : ",b[1:-1:1])
print("dot product :",np.dot(a,b))
print("sort of a :", np.sort(a))
print("sort of b :", np.sort(b))
print("sin of a :", np.sin(a))
print("sin of b :", np.sin(b))
print("log of a :", np.log(a))
print("log of b :", np.log(b))
print("dimension of a " , np.shape(a))
print("dimension of b " , np.shape(b))
print("reshape of a " , a.reshape(2,2))
print("reshape of b " , b.reshape(2,2))
print("transpose of a " , a.reshape(2,2).T)
print("transpose of b " , b.reshape(2,2).T)
print("maximum of a and b :" , np.maximum(a,b))
print("minimum of a and b :" , np.minimum(a,b))
print(" number of dimensions " ,a.ndim)
print(" shape of a  " ,a.shape )
print(" size of a  " ,a.size )
print("variance of a ", a.var())
print(" itemsize of a" ,a.itemsize )
print(" cumulative sum of a " ,np.cumsum(a) )
print(" cumulative product of a " ,np.cumprod(a) )  
print(" exponential of a " ,np.exp(a) )
print(" square root of a " ,np.sqrt(a) )
print(" logarithm base 10 of a " ,np.log10(a) )
print(" unique elements in a " ,np.unique(a) )
# Flattening in Python means converting a multi-dimensional structure into a single (1-D) sequence.
print(" flattening a  " ,a.flatten() )
print(" flattening b  " ,b.flatten() )
#merging two arrays a and b through concatenate (by c and by directly ) , vstack and hstack
print("c is concatenation of a and b  " ,c )
print(" concatenate a and b  " ,np.concatenate((a,b)) )
print(" stack a and b vertically  " ,np.vstack((a,b)) )
print(" stack a and b horizontally  " ,np.hstack((a,b)) )
print("intersection of a and b  " ,np.intersect1d(a,b) )
print("difference of a and b  " ,np.setdiff1d(a,b) )
print("checking if elements of a are in b  " ,np.isin(a,b) )
print("checking if elements of b are in a  " ,np.isin(b,a) )
print("stacking a and b column wise  " ,np.column_stack((a,b)) )
# np.row_stack() still works , but NumPy plans to reove it in the future  , so they recommend using np.vstack() instead print("stacking a and b row wise", np.row_stack((a, b)))
# sum of each column and row , row is axis 1 and column is axis 0
print("sum row", A.sum(axis=0)) 
print("sum col",A.sum(axis=1))
# mean of each column and row , row is axis 1 and column is axis 0  
print("mean row ",A.mean(axis=0)) 
print("mean col ",A.mean(axis=1))
# standard deviation of each column and row , row is axis 1 and column is axis 0
print("standard row ",A.std(axis=0)) 
print("standard col ",A.std(axis=1))    
# variance of each column and row , row is axis 1 and column is axis 0
print("variance row ",A.var(axis=0))        
print("variance col ",A.var(axis=1))
# cumulative sum of each column and row , row is axis 1 and column is axis 0
print("cumulative sum row ",np.cumsum(A, axis=0)) 
print("cumulative sum col",np.cumsum(A, axis=1))
# cumulative product of each column and row , row is axis 1 and column is axis      
print("cumulative product row",np.cumprod(A, axis=0)) 
print("cumulatice product col",np.cumprod(A, axis=1))
# transpose of a 2d array
print("transporse 2d ",A.T)  
# argsort returns the indices that would sort an array
print(np.argsort(a))
# searchsorted finds indices where elements should be inserted to maintain order
print(np.searchsorted(a, 2))
# printing numbers greater than 2 in array a
print(a[a > 2])
# creating identity matrix , eye creates a 2d array with 1's in diagonal and 0's elsewhere
print(np.identity(3))
# creating identity matrix of 3 rows and 4 columns
print(np.eye(3, 4))
# creating array of ones and zeros
print(np.ones((2,3)))
# creating array of zeros
print(np.zeros((2,3)))
# creating identity matrix with diagonal shifted by k positions
print(np.eye(3, 4, k=1))
X1 = np.array([1, 2, 3])
X2 = np.array([4, 5, 6])
X3 = np.c_[X1, X2]   # combine as columns
X4 = np.r_[X1, X2]  # combine as row 
print(X3)
print(X4)
