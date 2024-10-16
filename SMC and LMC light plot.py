import numpy as np
import matplotlib.pyplot as plt

class LightCurve:
    def __init__(self, data_points, target=None):
        self.data = self._process_data(data_points)
        self.target = target

    def _process_data(self, data_points):
        time, mag, is_upper_limit = [], [], []

        for point in data_points.strip().splitlines():
            try:
                t, m = point.split()
                t = float(t)

                if '<' in m:
                    m = float(m.replace('<', ''))
                    is_upper_limit.append(True)
                else:
                    m = float(m)
                    is_upper_limit.append(False)

                time.append(t)
                mag.append(m)
            except ValueError:
                print(f"Skipping invalid data point: {point}")

        # Store data in a structured array
        data = np.zeros(len(time), dtype=[('time', 'f4'), ('mag', 'f4'), ('is_upper_limit', '?')])
        data['time'] = time
        data['mag'] = mag
        data['is_upper_limit'] = is_upper_limit

        return data

    def get_time_flux(self):
        return self.data['time'], self.data['mag']

    def plot(self):
        time, flux = self.get_time_flux()
        plt.figure(figsize=(18.5, 10.5))
        # Plot regular data points
        plt.scatter(time[~self.data['is_upper_limit']], 
                    flux[~self.data['is_upper_limit']], 
                    color='darkblue', s=3)
        # Plot upper limits with downward arrows
        plt.scatter(time[self.data['is_upper_limit']], 
                    flux[self.data['is_upper_limit']], 
                    color='red', marker='v', s=3)  # 'v' for downward triangle
        plt.xlabel("Time (JD)")
        plt.ylabel("Magnitude")
        plt.title(f"Light Curve of {self.target}" if self.target else "Light Curve")
        plt.gca().invert_yaxis()  # Invert the y-axis
        plt.show()  # Display the plot

# Paste your JD and Mag data directly here
data_points = """

"""  # Add more data points as needed

# Create a LightCurve object and plot
light_curve = LightCurve(data_points, target="Sample Target")
light_curve.plot()




