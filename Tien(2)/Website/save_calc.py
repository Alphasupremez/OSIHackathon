import pandas as pd

class DisplaySavings:
    def __init__(self, filename, savings):
        self.saving_amount = savings
        self.file_name = filename
        self.saving = pd.read_csv(filename)

    def calculate_past_savings(self):
        add_save = pd.DataFrame({"Savings": [self.saving_amount]})
        self.saving = pd.concat([self.saving, add_save], ignore_index=True)
        last_save = self.saving['Savings'].iloc[-1]
        
        self.saving.to_csv(self.file_name, index=False)
    
    def total_savings(self):
        running_total = self.saving['Savings'].sum()
        return running_total