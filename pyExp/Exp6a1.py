#BAR GRAPH
import matplotlib.pyplot as plt
lst = ['English', 'Maths', 'History', 'Science', 'Geography', 'Others']
data = [25,46,98,107,73,63]
fig = plt.figure("SaxX")
plt.bar(lst, data, color="cyan")
fig.suptitle('Representing marks in each subject via a Bar Graph using matplotlib')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.xticks(fontsize=10)
#Customising the above bar graph

# fig2 = plt.figure()
# plt.grid(color='orange', linestyle='dashdot', linewidth=2, axis='y',alpha=0.7)
# plt.bar(lst, data, color='red', alpha=0.7)
# fig2.suptitle('Representing marks in each subject via a Bar Graph (Customised) using matplotlib')
# plt.xlabel('Subjects')
# plt.ylabel('Marks')
# plt.xticks(fontsize=10)
plt.show()