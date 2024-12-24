from singleTrail import SingleTril
import matplotlib.pyplot as plt
import pandas as pd


class GroupAnalysis:
    def __init__(self, in_path):
        self.in_path = in_path
        self.data = pd.read_csv(self.in_path, low_memory=False, dtype={
            'RECORDING_SESSION_LABEL': 'int32',
            'pupil baseline': 'str',
            'AVERAGE_PUPIL_SIZE_BIN': 'str'
        })

    def get_average_loads(self):
        participants = self.data['RECORDING_SESSION_LABEL'].unique()

        # Initialize lists to store all participants' data
        all_load1_data = []
        all_load4_data = []

        single_trial = SingleTril(self.in_path)

        for participant in participants:
            _, load1_data, _ = single_trial.load1data(participant)
            _, load4_data, _ = single_trial.load4data(participant)

            all_load1_data.append(load1_data)
            all_load4_data.append(load4_data)

        # Calculate averages
        avg_load1 = pd.DataFrame(all_load1_data).mean()
        avg_load4 = pd.DataFrame(all_load4_data).mean()

        return avg_load1, avg_load4

    def plot_group_averages(self):
        avg_load1, avg_load4 = self.get_average_loads()
        X_values = list(range(0, 6000, 50))

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6))

        # Plot average Load 1
        ax1.set_ylim(-2000, 2000)
        ax1.set_title("Group Average - Load 1")
        ax1.plot(X_values, avg_load1)
        ax1.grid(True)
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Difference from baseline', rotation=90)

        # Plot average Load 4
        ax2.set_ylim(-2000, 2000)
        ax2.set_title("Group Average - Load 4")
        ax2.plot(X_values, avg_load4)
        ax2.grid(True)
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Difference from baseline', rotation=90)

        plt.tight_layout()
        plt.show()


# Usage
group_analysis = GroupAnalysis("C:/Users/jasminee/Research/test.csv")
group_analysis.plot_group_averages()