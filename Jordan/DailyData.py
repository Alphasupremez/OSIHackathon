import pandas as pd

class DailyData:
    def __init__(self):
        self.energy_df = None
        self.save_time_df = pd.DataFrame(columns=['StartTime', 'EndTime', 'Rate'])
        
    def calculate_rates(self):
        self.energy_df = pd.read_csv('Jordan\\Energy.csv')
        for index, row in self.energy_df.iterrows():
            start_time = row['StartTime']
            end_time = row['EndTime']
            genlvl = row['GenLvl']
            genload = row['Generation'] - row['Load']
            if genload > 0:
                if genlvl == 'low':
                    rate = 0.5
                elif genlvl == 'med':
                    rate = 0.4
                elif genlvl == 'high':
                    rate = 0.3
            else:
                rate = 0.6
            save_row = pd.Series({'StartTime': start_time, 'EndTime': end_time, 'Rate': rate})
            self.save_time_df = self.save_time_df.append(save_row, ignore_index=True)
        self.save_time_df = self.save_time_df.drop(self.save_time_df.index[-1])
        return self.save_time_df



