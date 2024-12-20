# ELECTRIC VEHICLES DATA VISUALIZATION

This project consists of three tasks to visualize and analyze an electric vehicles dataset using various visualization techniques. The tasks involve creating grouped bar charts, bubble charts, and scatter plot matrices (SPLOMs) using Python scripts.

## DATASET

The dataset (`evs_assignment1.xlsx`) provides specifications for various electric vehicles, including attributes such as "Manufacturer," "Model," "Weight," "Top Speed," "Range," "Acceleration," "Efficiency," "Price," and "Region." The dataset is stored as an Excel workbook with 119 entries.

## PREREQUISITES

- **Python 3.11** or higher

Required Libraries: 
- **pandas** - 2.2.2
- **seaborn** - 0.13.2
- **matplotlib** - 3.9.2
- **argparse** - 1.1

Install the necessary libraries using:
```bash
pip install pandas seaborn matplotlib
```

## TASK 1
**Objective**

Create two grouped bar charts to visualize the efficiency distribution of electric vehicles by production region. The first chart shows absolute counts, and the second chart shows the relative distribution.

Script: p1_bars.py

### API Call

```bash
python p1_bars.py -i <filename>
```
filename: the path for the excel file the dataset is stored in

### EXAMPLE
```bash
python p1_bars.py -i evs_assignment1.xlsx
```

## TASK 2
**Objective**

Create a dynamic bubble chart to visualize the relationship between four different attributes of the electric vehicles. Each car is represented by a circle centered at (x=a1, y=a2), with the area corresponding to a3 and a color encoding a4.

Script: p1_bubbles.py

### API Call

```bash
python p1_bubbles.py -i <filename> -x <attribute> -y <attribute> -c <attribute> -s <attribute>
```
filename: the path for the excel file the dataset is stored in

-x attribute: the attribute to configure the x-axis

-y attribute: the attribute to configure the y-axis

-c attribute: the attribute to configure the color

-s attribute: the attribute to configure the size

### EXAMPLE
```bash
python p1_bubbles.py -i evs_assignment1.xlsx -x "Weight" -y "Range" -c "Top Speed" -s "Acceleration"
```

## TASK 3
**Objective**

Create a dynamic scatter plot matrix (SPLOM) to visualize the relationships between multiple attributes of electric vehicles, showing correlations between each pair of attributes. Seaborn is a Python data visualization library based on Matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics. In this task, Seaborn's pairplot function is used to create the scatter plot matrix (SPLOM)

Script: p1_splom.py

### API Call
```bash
python p1_splom.py -i <filename> -a <attribute> <attribute> <attribute> .... <attribute>
```
filename: the path for the excel file the dataset is stored in

-a attribute: the attributes to include in the SPLOM. You can specify up to 7 attributes.

### EXAMPLE
```bash
p1_splom.py -i evs_assignment1.xlsx -a "Weight" "Range" "Top Speed" "Acceleration"
```
