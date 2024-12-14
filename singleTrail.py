import matplotlib.pyplot as plt
import pandas as pd
import random

class SingleTril:
    def __init__(self, in_path):
        self.in_path = 'C:/firstYear/reaserch/exampleDataBase.csv'

    def participant_chosser(self, file):
        ### the function chooces a single participant randomly to show is data later on the plot ###
        data = pd.read_csv(file)  # reading CSV file
        participants = data['RECORDING_SESSION_LABEL'].tolist() # converting column data to list
        random_participant = random.choice(participants)
        return random_participant

    def data_creator(self):
        ###takes a random participant and puts his data in 2 lists - X and Y values###
        # takes only the random participant from participant_chosser func
        RECORDING_SESSION_LABEL = self.participant_chosser(self.in_path)
        data = pd.read_csv(self.in_path)
        filtered_data = data[(data['RECORDING_SESSION_LABEL'] == RECORDING_SESSION_LABEL) & (data['critical'] == 'y')]
        diff_values = filtered_data['diff from baseline']
        diff_values_list = diff_values.tolist()
        diff_values_list120 = diff_values_list[:120]
        return diff_values_list, diff_values_list120, str(RECORDING_SESSION_LABEL)

    def find_Max_Min(self):
        diff_value_list, not_relevant1, not_relevant2 = self.data_creator()
        min_val = min(diff_value_list)  # Using built-in min() function
        max_val = max(diff_value_list)  # Using built-in max() function
        return min_val, max_val

    def plot_creator(self):
        ### After taking the relevan data from a participant, plotting it ###
        X_values = list(range(0, 6000, 50))
        not_relevant, Y_values, random_participant = self.data_creator()

        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.ylim(-2000, 2000)
        plt.title("Random participant number" + " " + random_participant)
        plt.plot(X_values, Y_values)

        # Get min and max values
        min_val, max_val = self.find_Max_Min()

        # Add min and max values as text on the plot
        plt.text(0.02, 0.98, f'Max: {max_val:.2f}',
                 transform=plt.gca().transAxes,
                 verticalalignment='top',
                 bbox=dict(facecolor='white', alpha=0.8))

        plt.text(0.02, 0.02, f'Min: {min_val:.2f}',
                 transform=plt.gca().transAxes,
                 verticalalignment='bottom',
                 bbox=dict(facecolor='white', alpha=0.8))

        plt.grid(True)  # Added grid for better readability
        plt.xlabel('Time')  # Added axis labels
        plt.ylabel('Difference from baseline')

        plt.show()




