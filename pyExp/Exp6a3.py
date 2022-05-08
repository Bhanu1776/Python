#HISTOGRAM
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1,1)
x = np.random.normal(175, 15, 40)
ax.set_title("Height of 40 students in a class depicted in a Histogram")
ax.set_xticks([140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205])
ax.set_xlabel('Height')
ax.set_ylabel('No. of students')
plt.hist(x)
plt.show()