import matplotlib
import tkinter as tk
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

x_values = [1, 2, 3, 4]
y_values = [5, 4, 6, 2]

plt.scatter(x_values, y_values)

other_x_values = [1, 2, 3, 4]
other_y_values = [4, 2, 3, 9]

plt.plot(other_x_values, other_y_values, color='red')

plt.title("sample plot")

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()
