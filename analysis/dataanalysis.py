import matplotlib
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
from pandas import DataFrame, read_csv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=False, type=str, default='../debug/output3.txt',
                    help="Input file to read and process")
args = vars(ap.parse_args())
file_name=args["file"]
df = pd.read_csv(file_name,sep='\t')
keys=df.keys()
laser_values=df.query("sensor_type=='L'").copy()
print("Number of laser records={}".format(laser_values.count()))
radar_values=df.query("sensor_type=='R'").copy()
print("Number of radar records={}".format(radar_values.count()))
radar_values['chi_squared']= 7.815
laser_values['chi_squared']= 5.991
in_range_radar_values=radar_values.query("NIS>=0.35 & NIS<=7.815")
print("Number of radar values between 0.35 and 7.815={}".format(in_range_radar_values.count()))
fig = plt.figure(figsize=(9,4))
subfig1=fig.add_subplot(1,2,1)
subfig1.plot(radar_values[['NIS','chi_squared']])
subfig1.set_title('NIS for Radar Readings')

subfig1=fig.add_subplot(1,2,2)
subfig1.plot(laser_values[['NIS','chi_squared']])
subfig1.set_title('NIS for Laser Readings')
fig.tight_layout()
plt.show()
fig.savefig("NISlongx_xxyawx_xx.jpg",bbox_inches='tight')