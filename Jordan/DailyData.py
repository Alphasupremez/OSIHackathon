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
            index1 = row['Index']
            if genload > 0:
                if genlvl == 'low':
                    rate = 0.5
                elif genlvl == 'med':
                    rate = 0.4
                elif genlvl == 'high':
                    rate = 0.3
            else:
                rate = 0.6
            save_row = pd.Series({'Index': index1, 'StartTime': start_time, 'EndTime': end_time, 'Rate': rate})
            save_rows = save_row.to_frame().T
            self.save_time_df = pd.concat([self.save_time_df, save_rows], ignore_index=True)
        self.save_time_df = self.save_time_df.drop(self.save_time_df.index[-1])
        return self.save_time_df
