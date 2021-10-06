import matplotlib.pyplot as plt

x_values = range(1,1000)
y_values = [x**2 for x in x_values] #x**2 means x squared in the values of x

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)
#Set title and labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
#Set the range of the axes
ax.axis([0, 1100, 0, 1100000])

plt.show()