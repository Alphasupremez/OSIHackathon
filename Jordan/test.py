from DailyData import DailyData
import pandas as pd

d = DailyData()
t = d.calculate_rates()
print(t)