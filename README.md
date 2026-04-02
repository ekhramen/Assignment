# Assignment

 Assignment for J&J (Assignment.py)

This scipt aims to analyze the amount of carbon dioxide emission reduction due to the increase in the usage of the renewable energy technologies. The script cleans, prepares the data from the csv file and then preselects the desirable renewable energy source for further investigation. Ultimately the scipts creates the graph, which shows the total amount of the carbon dioxide avoided as a result of the increase in renewable enregy production.
This script is executed if the csv file is provided.

## Installation

```
git clone https://github.com/ekhramen/Assignment.git
```

* [example]: This folder contains the csv file used as a data source. The file originates from the StatLine website: https://opendata.cbs.nl/#/CBS/nl/dataset/84918NED/table?ts=1775069378743. In addition to the years of 2023 and 2024, the years starting from 2010 have been included in the dataset. The dataset was downloaded using the option: 'CSV met statistische symbolen'.
This script was created and executed using Spyder 5.0.5 and Python 3.9.6.
More information on Spyder could be found here: https://www.spyder-ide.org/

## Instructions

Provide the file_path to the location of the file containing the data. You can use the data source in the folder example or download it yourself from the original source with the years of choice: 
        ```
        https://opendata.cbs.nl/#/CBS/nl/dataset/84918NED/table?ts=1775069378743
        ```
The output of this script is a single bar plot showing the total amount of avoided carbon dioxide kton due to the implemented renewable energy technologies. The graph depicts the contribution of each renewable energy source to the total carbon dioxide reduction effect in years 2010 - 2024.
