# Evaluation of discomfort glare using physical measurements and behavioral data

This repository contains the following main folders and files :

* **Figures**: regroup all outputs of the plots used in the code.

* **Function**: regroup python files which automatize all the processes of preprocessing to deal with all the data in "2.Analysis.ipynb" (**start_time.py**: automatize the preprocessing (link to the time); **pupil_sizes.py**: automatize the calculation of the diameter of the pupil and **test_stats.py**: automatize the calculation of the Blink rate + test statistics)

* **1.Methodology_detailed.ipynb**: a methodology for one subject for Room 2243, where all the code is presented in detail.

* **2.Analysis.ipynb**: use the folder Function to present a complete analysis of all useable data csv from both room

## Data
In summer 2021, a laboratory study was conducted at the BP building at EPFL, in Lausanne, Switzerland. This study was supervised by Caroline Karmann, scientist at the Laboratory of Integrated Performance in Design (LIPID). The goal of this study is to investigate the effect of overall environmental conditions, glare and view
out on participants’ subjective responses, behavior and task performance. The different tests and the exact process of the experiment are described with more details in the report. The outputs of this study are regrouped in the following files and folders:

* **webcam_2021-07-20-16-49.csv**: This is the "csv" file containing the data for one subject for room 2243. ( This file is used to demonstrate our methodology)

* **2243**: regroup all the useable data of the same format as the one previously explained for room 2243.

* **2229**: regroup all the useable data of the same format as the one previously explained for room 2229. 

* **2243_txt_file_in_CSV.csv**: represent the data for room 2243 taken by hand from the supervisor of the study

* **2229_txt_file_in_CSV.csv**: represent the data for room 2229 taken by hand from the supervisor of the study

* **Data**: regroup others datasets added or created during the study ( **BP_Results_by_hand_v3_2021-11-12.xlsx** : excel file taken by hand from the supervisor of the study;**data_exposure_survey_small.csv**: represent the data of the survey taken by the subjects; **data_exposure_survey_with_objective_glare.csv**: represent the data from the survey with features on the glare; **survey_clean.csv**: csv created after the preprocessing to be easier to access and **weather_only.csv**: represent data on the weather during the study ).

## Getting Started

First, you will need to have " git " install on your computer to be able to clone the repository on your computer. You will also need to have python and jupyter notebook installed. If this is not the case you can download it from here: Python: https://www.python.org/downloads/  and for jupyter notebook the easiest is to download Anaconda: https://docs.anaconda.com/anaconda/install/index.html and open it from there.

## Dependencies and Installing

The code is using some Python libraries: "Numpy" and "Pandas" to analyze data, "Matplotlib" and "Seaborn" to visualize the output of the analysis, and "Scipy" for the statistical analysis.

If you are completely new to those libraries. The easiest way is to use "conda" command in your terminal, once you have downloaded Anaconda. Those can also be downloaded in some other way. More information is provided on their websites

If you are using anaconda, you can simply copy those code lines on your terminal.

* pandas : 
```
conda install -c anaconda pandas
```

* matplotlib :

```
conda install matplotlib
```
* numpy : 
```
conda install -c anaconda numpy
```
* Scipy
```
conda install -c anaconda scipy
```


### Executing program

To execute the program you need to follow the steps described below:
* Clone the repository on your computer
* Get the Python libraries needed
* Enter in the repository with this command (Windows) or equivalent code line for Mac and Linux
```
cd enac_project
```
* Run jupyter lab as follow in the command line:
```
jupyter lab 
```

* Another way to open the repository that you have cloned is to open Anaconda Navigator and open it from there.


## Authors

Simon Dayer and Quentin Bochud

