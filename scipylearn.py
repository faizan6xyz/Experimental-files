import numpy as np
import pandas as pd

# ---------------- INTEGRATION ----------------
from scipy import integrate

result, err = integrate.quad(lambda x: x**2, 0, 3)
print("Integration result:", result)

# double integration example
result2, err2 = integrate.dblquad(lambda y, x: x*y, 0, 1, lambda x: 0, lambda x: 1)
print("Double Integration:", result2)


# ---------------- LINEAR ALGEBRA ----------------
from scipy import linalg

A = np.array([[1,2],[3,4]])

inv = linalg.inv(A)
print("Inverse matrix:\n", inv)

det = linalg.det(A)
print("Determinant:", det)

eigenvalues, eigenvectors = linalg.eig(A)
print("Eigenvalues:", eigenvalues)


# ---------------- OPTIMIZATION ----------------
from scipy import optimize

f = lambda x: x**2 + 5*x + 6

res = optimize.minimize(f, 0)
print("Minimum point:", res.x)

# find root
root = optimize.root(lambda x: x**2 - 4, 0)
print("Root:", root.x)


# ---------------- STATISTICS ----------------
from scipy import stats

data = [10,20,30,40,50]

print("Mean:", stats.tmean(data))
print("Standard Deviation:", stats.tstd(data))
print("Median:", stats.median_abs_deviation(data))
print("Variance:", stats.tvar(data))


# ---------------- FOURIER TRANSFORM ----------------
from scipy.fft import fft

data_fft = [0,1,0,0]

result_fft = fft(data_fft)
print("FFT:", result_fft)


# ---------------- INTERPOLATION ----------------
from scipy import interpolate

x = np.arange(5)
y = x**2

f_interp = interpolate.interp1d(x,y)

print("Interpolation at 2.5:", f_interp(2.5))


# ---------------- RANDOM DISTRIBUTION ----------------
from scipy.stats import norm

r = norm.rvs(size=5)
print("Random Normal Values:", r)

pdf = norm.pdf(0)
print("Normal PDF at 0:", pdf)