import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Generate a SPLOM for EV data.')
parser.add_argument('-i', '--input', type=str, required=True, help='Input file name with path')
parser.add_argument('-a', '--attributes', type=str, nargs='+', required=True, help='Attributes to include in the SPLOM')
args = parser.parse_args()

if len(args.attributes) > 7:
    print("Error: You can only specify up to 7 attributes for the SPLOM.")
    exit(1)

ev = pd.read_excel(args.input)

#subset df to include only selected attributes and the region 
ev_subset = ev[args.attributes + ['Region']]

color_palette = {'America': '#be1558', 'Asia': '#fbcbc9', 'Europe': '#322514'}

g = sns.pairplot(ev_subset, hue='Region', palette=color_palette, plot_kws={'alpha': 0.6, 's': 40}, diag_kind='auto')

num_attributes = len(args.attributes)

g.fig.suptitle(f'Scatter Plot Matrix of {num_attributes} EV attributes', y=1.00)

plt.draw()
plt.pause(0.1)
plt.show()