import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("atten.csv")
rollno = df['Roll_no'].values
x = np.arange(len(rollno))
w = 1
plt.bar(x, df['Sub1'].values, color = "lavender")
plt.xticks(x, rollno,rotation='90')
plt.title("SUBJECT 1")
plt.show()
plt.bar(x, df['Sub2'].values, color = "mistyrose")
plt.xticks(x, rollno,rotation='90')
plt.title("SUBJECT 2")
plt.show()
plt.bar(x, df['Sub3'].values, color = "lightgreen")
plt.xticks(x, rollno,rotation='90')
plt.title("SUBJECT 3")
plt.show()
plt.bar(x, df['Sub4'].values, color = "powderblue")
plt.xticks(x, rollno,rotation='90')
plt.title("SUBJECT 4")
plt.show()
plt.bar(x, df['Sub5'].values, color = "thistle")
plt.xticks(x, rollno,rotation='90')
plt.title("SUBJECT 5")
plt.show()