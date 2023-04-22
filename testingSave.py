from save_calc import *

savings = 0.3

filename = "savings.csv"

ds = DisplaySavings(filename, savings)

cps = ds.calculate_past_savings()

ts = ds.total_savings()

saving = pd.read_csv(filename)

ps = saving['Savings'].iloc[-1]

print(saving)
print(f"Your total savings are {ts}")
print(f"Your last saving amount was {ps}")