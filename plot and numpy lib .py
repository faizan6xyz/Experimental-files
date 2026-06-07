import matplotlib.pyplot as plt
import numpy as np
# ---------------- LINE PLOT ----------------
# Use: Shows trends or continuous data over time
x = np.linspace(0,10,100)
y = np.sin(x)
plt.plot(x,y)
plt.title("Line Plot")
plt.xlabel("X values")
plt.ylabel("sin(x)")
plt.show()
# ---------------- TAN LINE PLOT ----------------
# Use: Shows relationship between variables
a = np.linspace(0,10,100)
b = np.tan(a)
plt.plot(a,b)
plt.title("Tan Line Plot")
plt.xlabel("a values")
plt.ylabel("tan(a)")
plt.show()
# ---------------- SCATTER PLOT ----------------
# Use: Shows relationship between two variables
x = np.random.rand(150)
y = np.random.rand(150)
plt.scatter(x,y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
# ---------------- BAR PLOT ----------------
# Use: Compare values between different categories
categories = ["A","B","C","D","E"]
values = [1,2,3,4,2]
plt.bar(categories,values)
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
# ---------------- HISTOGRAM ----------------
# Use: Shows distribution of data
data = np.random.randn(1000)
plt.hist(data,bins=30,color='skyblue',edgecolor='black')
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
# ---------------- BOX PLOT ----------------
# Use: Shows spread of data and detects outliers
np.random.seed(10)
d = np.random.normal(100,20,200)
plt.boxplot(d)
plt.title("Box Plot")
plt.show()
# ---------------- PIE CHART ----------------
# Use: Shows percentage distribution of categories
labels = ['A','B','C','D']
sizes = [20,30,25,25]
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
# ---------------- AREA PLOT ----------------
# Use: Shows cumulative trends
x = np.arange(1,6)
y = [1,4,6,8,10]
plt.fill_between(x,y)
plt.title("Area Plot")
plt.xlabel("X")
plt.ylabel("Values")
plt.show()
# ---------------- STEM PLOT ----------------
# Use: Displays discrete data points (signal processing)
x = np.arange(10)
y = x**2
plt.stem(x,y)
plt.title("Stem Plot")
plt.show()
# ---------------- STEP PLOT ----------------
# Use: Shows stepwise changes in data
x = np.arange(10)
y = np.random.randint(1,10,10)
plt.step(x,y)
plt.title("Step Plot")
plt.show()
# ---------------- ERROR BAR PLOT ----------------
# Use: Shows measurement uncertainty
x = np.arange(5)
y = [5,7,9,11,13]
error = [1,1.5,1,2,1]
plt.errorbar(x,y,yerr=error)
plt.title("Error Bar Plot")
plt.show()
# ---------------- STACK PLOT ----------------
# Use: Shows composition of data over time
x = np.arange(1,6)
y1 = [1,2,3,4,5]
y2 = [2,3,4,3,2]
plt.stackplot(x,y1,y2)
plt.title("Stack Plot")
plt.show()