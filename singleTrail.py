import matplotlib.pyplot as plt
import pandas as pd

class SingleTril:
    def __init__(self, in_path):
        self.in_path = in_path
        self.data = pd.read_csv(self.in_path, low_memory=False, dtype={
            'RECORDING_SESSION_LABEL': 'int32',
            'pupil baseline': 'str',
            'AVERAGE_PUPIL_SIZE_BIN': 'str'
        })

    def load4data(self, RECORDING_SESSION_LABEL):
        data = self.data
        filtered_data = data[(data['RECORDING_SESSION_LABEL'] == RECORDING_SESSION_LABEL) & (data['critical'] == 'y') & (data['load'] == 4)]
        diff_values = filtered_data['diff from baseline']
        diff_values_list = diff_values.tolist()
        diff_values_list120 = diff_values_list[:120]
        return diff_values_list, diff_values_list120, str(RECORDING_SESSION_LABEL)

    def load1data(self, RECORDING_SESSION_LABEL):
        data = self.data
        filtered_data = data[(data['RECORDING_SESSION_LABEL'] == RECORDING_SESSION_LABEL) & (data['critical'] == 'y') & (data['load'] == 1)]
        diff_values = filtered_data['diff from baseline']
        diff_values_list = diff_values.tolist()
        diff_values_list120 = diff_values_list[:120]
        return diff_values_list, diff_values_list120, str(RECORDING_SESSION_LABEL)
    #

    def find_Max_Min(self, participant):
        diff_value_list, not_relevant1, not_relevant2 = self.load4data(participant)
        min_val = min(diff_value_list)  # Using built-in min() function
        max_val = max(diff_value_list)  # Using built-in max() function
        return min_val, max_val

    def plot_creator(self, participant):
        X_values = list(range(0, 6000, 50))
        # Get data for both loads
        not_relevant1, Y_values_load1, _ = self.load1data(participant)
        not_relevant4, Y_values_load4, _ = self.load4data(participant)

        # Create figure with two subplots side by side
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6))

        # Plot Load 1
        ax1.set_ylim(-2000, 2000)
        ax1.set_title(f"Participant {participant} - Load 1")
        ax1.plot(X_values, Y_values_load1)
        ax1.grid(True)
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Difference from baseline')

        # Plot Load 4
        ax2.set_ylim(-2000, 2000)
        ax2.set_title(f"Participant {participant} - Load 4")
        ax2.plot(X_values, Y_values_load4)
        ax2.grid(True)
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Difference from baseline')

        plt.tight_layout()
        plt.show()


# test = SingleTril("C:/Users/jasminee/Research/test.csv")
# test.plot_creator(430)






