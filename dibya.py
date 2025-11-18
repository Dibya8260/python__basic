import matplotlib.pyplot as plt

# Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# # Plot
# plt.plot(x, y)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Simple Line Graph")
# plt.show()
# import matplotlib.pyplot as plt

# subjects = ["Math", "Science", "English"]
# marks = [90, 85, 78]

# plt.bar(subjects, marks)
# plt.title("Marks of Subjects")
# plt.ylabel("Marks")
# plt.show()
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 1, 5, 3]

# plt.scatter(x, y)
# plt.title("Scatter Plot")
# plt.show()
# import matplotlib.pyplot as plt

# data = [22, 25, 30, 35, 27, 28, 32, 31, 29]

# plt.hist(data, bins=5)
# plt.title("Histogram Example")
# plt.show()
# import matplotlib.pyplot as plt

# x=[1,2,3]
# y1=[2,4,1]
# y2=[3,1,3]
# plt.plot(x,y1,lable='line 1')
# plt.plot(x,y2,lable='line 2')
# plt.legend(loc='upper left')
# plt.show()
import matplotlib.pyplot as plt

# plt.plot([1, 2, 3], [2, 4, 6], label="Line 1")
# plt.plot([1, 2, 3], [1, 3, 5], label="Line 2")

# plt.legend(loc='upper left')   # shows legend box
# plt.show()
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.xlim(0,6)
plt.ylim(bottom=0)
plt.plot(x,y)
plt.show()