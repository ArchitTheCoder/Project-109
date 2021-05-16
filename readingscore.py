from os import stat
import random
import statistics
from numpy import median
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data2.csv")
readingscore_list = df["reading score"].tolist()

mean = statistics.mean(readingscore_list)
median = statistics.median(readingscore_list)
mode = statistics.mode(readingscore_list)
std_dev = statistics.stdev(readingscore_list)

# print("Mean, median, mode, and std_dev of readingscore is {}, {}, {}, {} respectively".format(mean, median, mode, std_dev))

readingscore_first_std_dev_start, readingscore_first_std_dev_end = mean - \
    std_dev, mean + std_dev
readingscore_second_std_dev_start, readingscore_second_std_dev_end = mean - \
    (2 * std_dev), mean + (2 * std_dev)
readingscore_third_std_dev_start, readingscore_third_std_dev_end = mean - \
    (3 * std_dev), mean + (3 * std_dev)

readingscore_list_of_data_within_1_stddev = [result for result in readingscore_list if result >
                                             readingscore_first_std_dev_start and result < readingscore_first_std_dev_end]
readingscore_list_of_data_within_2_stddev = [result for result in readingscore_list if result >
                                             readingscore_second_std_dev_start and result < readingscore_second_std_dev_end]
readingscore_list_of_data_within_3_stddev = [result for result in readingscore_list if result >
                                             readingscore_third_std_dev_start and result < readingscore_third_std_dev_end]

fig = ff.create_distplot([readingscore_list], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[readingscore_first_std_dev_start, readingscore_first_std_dev_start], y=[0, 0.17], mode="lines", name="Std_dev 1"))
fig.add_trace(go.Scatter(x=[readingscore_first_std_dev_end, readingscore_first_std_dev_end], y=[0, 0.17], mode="lines", name="Std_dev 1"))
fig.add_trace(go.Scatter(x=[readingscore_second_std_dev_start, readingscore_second_std_dev_start], y=[0, 0.17], mode="lines", name="Std_dev 2"))
fig.add_trace(go.Scatter(x=[readingscore_second_std_dev_end, readingscore_second_std_dev_end], y=[0, 0.17], mode="lines", name="Std_dev 2"))
fig.add_trace(go.Scatter(x=[readingscore_third_std_dev_start, readingscore_third_std_dev_start], y=[0, 0.17], mode="lines", name="Std_dev 3"))
fig.add_trace(go.Scatter(x=[readingscore_third_std_dev_end, readingscore_third_std_dev_end], y=[0, 0.17], mode="lines", name="Std_dev 3"))
fig.show()

print("{}% of data for readingscore lies within 1 standard deviation".format(
    len(readingscore_list_of_data_within_1_stddev)*100.0/len(readingscore_list)))
print("{}% of data for readingscore lies within 2 standard deviation".format(
    len(readingscore_list_of_data_within_2_stddev)*100.0/len(readingscore_list)))
print("{}% of data for readingscore lies within 3 standard deviation".format(
    len(readingscore_list_of_data_within_3_stddev)*100.0/len(readingscore_list)))
