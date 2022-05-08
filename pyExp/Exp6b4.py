#Filtering in DataFrames
import pandas as pd
data = {
"calories": [450, 380, 390, 460, 410, 330, 440, 470, 480, 400],
"duration(mins)": [50, 37, 40, 55, 45, 31, 49, 59, 75, 43]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3", "day4", "day5", "day6", "day7", "day8", "day9", "day10"])
print(df[df.calories > 420])