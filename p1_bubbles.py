import matplotlib.pyplot as plt
import pandas as pd
import argparse

#dynamic for any attributes in any order
parser = argparse.ArgumentParser(description='Generate a bubble chart for EV data.')
parser.add_argument('-i', '--input', type=str, required=True, help='Input file name with path')
parser.add_argument('-x', '--xaxis', type=str, required=True, help='Attribute for the x-axis')
parser.add_argument('-y', '--yaxis', type=str, required=True, help='Attribute for the y-axis')
parser.add_argument('-c', '--color', type=str, required=True, help='Attribute for the color')
parser.add_argument('-s', '--size', type=str, required=True, help='Attribute for the size')
args = parser.parse_args()

ev = pd.read_excel(args.input)
x = ev[args.xaxis]
y = ev[args.yaxis]
color = ev[args.color]
size = ev[args.size]

size = size / size.max() * 1000 #scaling 

plt.figure(figsize=(10, 6))
scatter = plt.scatter(x=x, y=y, s=size, c=color, alpha=0.6, cmap='viridis') 

cbar = plt.colorbar(scatter)
cbar.set_label(args.color)

plt.xlabel(args.xaxis)
plt.ylabel(args.yaxis)
plt.title(f'Bubble Chart representation of {args.xaxis}, {args.yaxis}, {args.size}, {args.color}')

plt.show()