from .DailyData import DailyData
from pandas import *

class Saving:
    #STATIC ATTRIBUTES
    data = DailyData()
    save_time = data.calculate_rates()

    def __init__(self, startTime, endTime, rate):
    #CLASS ATTRIBUTES
        self.start_time = float(startTime)
        self.end_time = float(endTime)
        self.user_rate = float(rate)
        self.actual_paid = 0.0
        self.paid_saving = 0.0
        self.saving = 0.0
        self.saving_rate = 0.0
    
    #CLASS METHODS
    
    #THIS FUNCTION DOES EXACTLY WHAT IT SAYS
    #NO PARAMETERS
    def compute_saving(self):
        try:
            # assert self.start_time <= 2300 or self.start_time > -1,"time {} doesn't exist".format(self.start_time)
            # assert self.end_time <= 2300 or self.end_time > -1,"time {} doesn't exist".format(self.end_time)
        
            for index,row in Saving.save_time.iterrows():
                if (self.start_time / 100) < row["Index"] and self.saving_rate == 0:
                    self.saving_rate = row["Rate"]
            self.actual_paid = ((self.end_time - self.start_time) / 100) * self.user_rate
            self.paid_saving = ((self.end_time - self.start_time) / 100) * self.saving_rate
            self.saving = self.actual_paid - self.paid_saving
            self.saving_rate = 0
            return self.saving
        except AssertionError as msg:
            print(msg)
        
    