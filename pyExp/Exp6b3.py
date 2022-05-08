#Indexing in DataFrames
import pandas as pd
data = {
"calories": [460, 480, 450],
"duration(mins)": [60, 70, 50]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df.loc["day3"])