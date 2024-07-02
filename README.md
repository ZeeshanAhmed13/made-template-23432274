### Exercise Badges

![](https://byob.yarr.is/ZeeshanAhmed13/made-template-23432274/score_ex1) ![](https://byob.yarr.is/ZeeshanAhmed13/made-template-23432274/score_ex2) ![](https://byob.yarr.is/ZeeshanAhmed13/made-template-23432274/score_ex3) ![](https://byob.yarr.is/ZeeshanAhmed13/made-template-23432274/score_ex4) ![](https://byob.yarr.is/ZeeshanAhmed13/made-template-23432274/score_ex5)

### Project Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)	[![CI/CD](https://github.com/ZeeshanAhmed13/made-template-23432274/actions/workflows/github_action_project_test.yml/badge.svg)](https://github.com/ZeeshanAhmed13/made-template-23432274/actions/workflows/github_action_project_test.yml)	[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)



### Methods of Advanced Data Engineering Project

# Title: Analysis and visualization of agricultural data based on the impact of climate change through ETL process.

![Cover Photo](https://github.com/ZeeshanAhmed13/made-template-23432274/blob/main/Visuals%20and%20Diagrams/cover%20image.jpg)


## Project Description:
Climate change is increasingly reshaping agricultural landscapes worldwide, posing significant challenges to food security and crop productivity. The effects of rising mean surface temperatures are particularly evident in countries with diverse agricultural practices and climatic conditions. The impact of climate change on crop yield varies by region temperate regions, tropical and subtropical regions. Nevertheless, understanding the complex relation between climate and agricultural data remains a barrier, which needs an efficient data analysis and visualization framework. For this purpose, the objective of this project is to build an ETL pipeline to assess the impact of climate change on agricultural data and provide necessary valuable insights. The pipeline will collect various public datasets including historical climate data such as temperature, and different crops yield records. The extracted data will undergo several transformations to standardize formats, filling missing values and integrate relevant variables. Accordingly, the loaded data will be analyzed using statistical techniques to identify trends, correlations, irregularity caused by climate change effects on crop yield variability. The time series plots is utilized to effectively provide insights and patterns derived from the analysis. This framework will empower policymakers, and researchers on how to handle the difficulties arising from climate change in agriculture by providing them with well-informed decision-making capabilities.

### Main Questions:
- 1. What impact has climate change based on mean surface temperature variation had on crop yield in countries with diverse climates like Pakistan, Germany, Turkey, and Australia in the last years?
- 2. Have there been any trends or recurring patterns, in the yields of key crops such as maize, carrots, turnips, rice, and grapes?

## Data Sources:

### DataSource-1: Crop Production
- #### Metadata URL: https://data.world/agriculture/crop-production
- #### Data URL:
	- [Production_Crops_E_Africa.csv](https://query.data.world/s/3ibkgfh656yrydhmsg4uboxxm7hysr?dws=00000)
	- [Production_Crops_E_Americas.csv](https://query.data.world/s/2x6uq5jmauvfnmfhc5ud4jv5amq4p6?dws=00000)
	- [Production_Crops_E_Asia.csv](https://query.data.world/s/nc25wfakg22iva2tmkx4icgfnufggx?dws=00000)
	- [Production_Crops_E_Europe.csv](https://query.data.world/s/fglgedqxdxc2giqvqgvbjxsqic2tuw?dws=00000)
	- [Production_Crops_E_Oceania.csv](https://query.data.world/s/wva7g5yxspu3bninh4ucn7xrp4h6sc?dws=00000)

- #### Data Type: CSV
- #### Licence: CC BY-NC-SA
- #### DataSource Description:
	- The Food and Agriculture Organization of the United Nations (FAO) dataset provides comprehensive global crop production statistics for 173 products, categorized into cereals, vegetables, fruits, treenuts, fibre crops, oil crops, pulses, roots and tubers, among others. It includes data on area harvested, production quantity, yield, and seed quantity. The dataset aims to offer a detailed overview of primary crop production worldwide, aiding in the analysis of agricultural productivity, food security, and related economic factors.

- #### Source:
	- This dataset is taken from [FAO](https://www.fao.org/faostat/en/#data/QCL/visualize) and is used purely for project work only.

### DataSource-2: All Countries Temperature Statistics 1970-2021
- #### * Metadata URL: https://www.kaggle.com/datasets/mdazizulkabirlovlu/all-countries-temperature-statistics-1970-2021
- #### Data URL:
	- [Temperature_data.csv](https://www.kaggle.com/datasets/mdazizulkabirlovlu/all-countries-temperature-statistics-1970-2021?select=all+countries+global+temperature.csv)
- #### Data Type: CSV
- #### Licence: CC0 1.0 DEED
- #### DataSource Description:
	- This dataset provides details about global surface temperature changes from 1970 to 2021 across countries worldwide. It spans 51 years and compiles data from weather stations, satellites, and ocean buoys. The dataset enables analysis of temperature trends and identification of regions vulnerable to temperature changes, aiding in understanding climate change impacts and informing mitigation policies. Temperature is measured in degrees Celsius, with a positive index indicating an increase and a negative index indicating a decrease.

- #### Acknowledgment:
	- This data is provided by the Food and Agriculture Organization Corporate Statistical Database [FAOSTAT](https://www.fao.org/faostat/en/#home) and is based on publicly available GISTEMP data from the National Aeronautics and Space Administration Goddard Institute for Space Studies [NASA GISS](https://data.giss.nasa.gov/).

- #### Source:
	- Annual Surface Temperature Change: https://climatedata.imf.org/pages/climate-and-weather#cc1

- #### Citation:
	- International Monetary Fund. 2022. Climate Change Indicators Dashboard. Annual Surface Temperature Change, https://climatedata.imf.org/pages/access-data. Accessed on [2024-05-23].

#### Note: 
	This work is purely non-commercial and is used for only a semester project at FAU to implement the ETL pipeline and provide valuable insights.

## ETL Pipeline Structure:

The project follows a structured ETL (Extract, Transform, Load) pipeline approach stored in `/project/ETL_Pipelene.py`, which serves as the entry point for running the pipeline using the command `python3 ./project/ETL_Pipelene.py`.

- The ETL pipeline is built with Python3 to extract publicly available datasets including crop production data from datasource-1 and historical temperature records from datasource-2.
- The extracted data undergoes transformations to standardize the formats, integrate relevant variables, and fill missing values using linear interpolation and forward filling.
- The "Country Name" is used as the key to merge dataframes, retaining only entries with matching country names, crops of interest, and temperature readings year-wise, focusing on the years 1970 to 2019.
- Logging is additionally configured in the ETL pipeline to capture the process flow and record errors, tracking successful steps and issues; try-except blocks handle exceptions, stopping the process, and logging critical errors as needed.
- Also ensured a clean environment by checking for and removing the Kaggle dataset file after reading.
- The loaded data will be analyzed to identify trends, correlations, and irregularities caused by climate change effects on crop yield variability.


![ETL Pipeline Diagram](https://github.com/ZeeshanAhmed13/made-template-23432274/blob/main/Visuals%20and%20Diagrams/ETL_Pipeline_Overview.jpg)

Before you begin, make sure you have [Python3](https://www.python.org/) installed and set up [VSCode](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).


### Run Pipeline Locally

1. Clone the project

```
  git clone https://github.com/ZeeshanAhmed13/made-template-23432274.git
```

2. Go to the project directory

```
  cd made-template-23432274
```

3. Installing Dependencies

```
  pip install -r requirements.txt
```

4. Run the bash script `project/pipeline.sh`

```
  bash project/pipeline.sh
```

This will start a virtual environment and finally create a SQL database out of data sources named `pipeline` in the `\data` directory.

### Running Tests

To run tests, run the following command

```
  bash project/tests.sh
```

### Optional
1. Run and explore the report at "./project/analysis.ipynb"
2. Also can check the related [slides](https://github.com/ZeeshanAhmed13/made-template-23432274/slides.pdf) of the project and project [presentation video](https://github.com/ZeeshanAhmed13/made-template-23432274)



## Exercises
You will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

You will therefore have the following files in your repository:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.jv`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.jv`
5. `./exercises/exercise5.jv`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
