import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Generate grouped bar charts for EV efficiency data.')
parser.add_argument('-i', '--input', type=str, required=True, help='Input file name with path')
args = parser.parse_args()

ev = pd.read_excel(args.input)
bins = [100, 140, 180, 220, 260, 280]
ev['Efficiency Interval'] = pd.cut(ev['Efficiency'], bins=bins, right = False)
grouped = ev.groupby(['Efficiency Interval', 'Region']).size().unstack(fill_value=0)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

#graph1
grouped.plot(kind='bar', stacked=False, ax=axes[0], color=['#be1558', '#fbcbc9', '#322514'])
axes[0].set_title('Efficiency of EVs produced between 2010 and 2024 (Absolute)')
axes[0].set_xlabel('Efficiency in Wh/km')
axes[0].set_ylabel('Number of EV models')

#graph2
total_by_region = grouped.sum()

#relative fraction
relative_grouped = grouped.div(total_by_region, axis=1).fillna(0)

relative_grouped.plot(kind='bar', stacked=False, ax=axes[1], color=['#be1558', '#fbcbc9', '#322514'])
axes[1].set_title('Efficiency of EVs produced between 2010 and 2024 (Relative)')
axes[1].set_xlabel('Efficiency in Wh/km')
axes[1].set_ylabel('Proportion of EV models')
plt.tight_layout() #to get it in one window
plt.show()