import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("train.csv")
df.head(10)
df_male = (df["Sex"] == "male")
df_cabin_male = df["Cabin"].notnull()
df_age_male = df["Age"] < 50
print(df[df_male & df_cabin_male & df_age_male])
w = 0.4
xLabel = ["Male", "Female"]
maleSurvived = df[df["Sex"] == 'male']["Survived"].value_counts()
femaleSurvived = df[df["Sex"] == 'female']["Survived"].value_counts()
Male = [maleSurvived[0], femaleSurvived[0]]
Female = [maleSurvived[1], femaleSurvived[0]]
print(maleSurvived[0], maleSurvived[1], femaleSurvived[0], femaleSurvived[1])
bar1 = np.arange(len(xLabel))
bar2 = [i+w for i in bar1]
plt.bar(bar1, Male, w, label="Survived")
plt.bar(bar2, Female, w, label="Death")
plt.grid(color='blue', linestyle='dashdot', linewidth=2, axis='y', alpha=0.7)
plt.xlabel("")
plt.ylabel("")
plt.xticks(bar1+w/2, xLabel)
plt.legend()
plt.show()
