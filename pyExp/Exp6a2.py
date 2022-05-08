#PIE CHART
import matplotlib.pyplot as plt
lst = 'English', 'Maths', 'History', 'Science', 'Geography', 'Others'
users = [24,96,78,100,56,43]
fig1, ax1 = plt.subplots()
ax1.pie(users, labels = lst, autopct = '%1.1f%%', shadow = True, startangle = 0)
ax1.axis('equal')
plt.title("Marks of Individual Subject via a Pie Chart", bbox ={'facecolor':'0.8'}, y = 1.1)
plt.legend(bbox_to_anchor=(1,1))
plt.show()