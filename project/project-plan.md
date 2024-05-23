# Project Plan

## Title
<!-- Give your project a short title. -->
Analysis and Visualization of Agricultural Data based on the impact of Climate Change through ETL process.


## Main Question

<!-- Think about one main question you want to answer based on the data. -->

1. What impact has climate change based on temperature and rainfall pattern had on crop production in countries around the world in the last decades? Have there been any trends or recurring patterns, in crop yields?

2. Are there any considerable shifts in the geographical crops distribution as a result of changes in climatic conditions?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->

<p style="text-align: justify;">Climate change implies significant challenges to agricultural productivity worldwide, impacting crop yields. Nevertheless, understanding the complex relation between climate and agricultural data remains a barrier, which needs an efficient data analysis and visualization framework. For this purpose, the objective of this project is to build an ETL pipeline to assess or measure the impact of climate change on agricultural data and provide necassary valuable insights. The pipeline will collect various public datasets including historical climate data such as temperature and rainfall, and different crops yield records. The extracted data will undergo several transformations to standardize formats, clean outliers, filling missing values and integrate relevant variables. Accordingly, the loaded data will be analyzed using statistical techniques to identify trends, correlations, irregularity caused by climate change effects on crop yield variability. The time series plots, heatmaps, and geographical maps as visualization techniques is utilized to effectively provide insights and patterns derived from the analysis. This framework will empower policymakers, and researchers on how to handle the difficulties arising from climate change in agriculture by providing them with well-informed decision-making capabilities.</p>


## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### DataSource-1: Crop Production

#### * Metadata URL: https://data.world/agriculture/crop-production

#### * Data URL: 

1. Production_Crops_E_Africa.csv
    https://query.data.world/s/3ibkgfh656yrydhmsg4uboxxm7hysr?dws=00000

2. Production_Crops_E_Americas.csv
    https://query.data.world/s/2x6uq5jmauvfnmfhc5ud4jv5amq4p6?dws=00000

3. Production_Crops_E_Asia.csv
    https://query.data.world/s/nc25wfakg22iva2tmkx4icgfnufggx?dws=00000

4. Production_Crops_E_Europe.csv
    https://query.data.world/s/fglgedqxdxc2giqvqgvbjxsqic2tuw?dws=00000

5. Production_Crops_E_Oceania.csv
    https://query.data.world/s/wva7g5yxspu3bninh4ucn7xrp4h6sc?dws=00000

#### * Data Type: CSV

#### * Licence: CC BY-NC-SA

#### * DataSource Description:

  <p style="text-align: justify;">The Food and Agriculture Organization of the United Nations (FAO) dataset provides comprehensive global crop production statistics for 173 products, categorized into cereals, vegetables, fruits, treenuts, fibre crops, oil crops, pulses, roots and tubers, among others. It includes data on area harvested, production quantity, yield, and seed quantity. Notably, it covers only dry grain cereals, vegetables grown for human consumption (excluding those for animal feed), fresh fruit production primarily for sale (excluding home consumption and wild plants), and treenuts for sale (excluding those for oil extraction and flavoring). The dataset aims to offer a detailed overview of primary crop production worldwide, aiding in the analysis of agricultural productivity, food security, and related economic factors.</p>

#### Source: 
This dataset is taken from [(FAO)](https://www.fao.org/faostat/en/#data/QCL/visualize) and is used purely for project work only.


### DataSource-2: All Countries Temperature Statistics 1970-2021

#### * Metadata URL: https://www.kaggle.com/datasets/mdazizulkabirlovlu/all-countries-temperature-statistics-1970-2021

#### * Data URL: 

1. https://www.kaggle.com/datasets/mdazizulkabirlovlu/all-countries-temperature-statistics-1970-2021?select=all+countries+global+temperature.csv

#### * Data Type: CSV

#### * Licence: CC0 1.0 DEED

#### * DataSource Description:

  <p style="text-align: justify;">This dataset provide details about global surface temperature changes from 1970 to 2021 across countries around the world. It spans 51 years and compiles data from weather stations, satellites, and ocean buoys. The dataset enables analysis of temperature trends and identification of regions vulnerable to temperature changes, aiding in understanding climate change impacts and informing mitigation policies. Temperature is measured in degrees Celsius, with a positive index indicating an increase and a negative index indicating a decrease.</p>

#### Acknowledgment: 

This data is provided by the Food and Agriculture Organization Corporate Statistical Database [(FAOSTAT)](https://www.fao.org/faostat/en/#home) and is based on publicly available GISTEMP data from the National Aeronautics and Space Administration Goddard Institute for Space Studies [(NASA GISS)](https://data.giss.nasa.gov/).

#### Source: 

- **Annual Surface Temperature Change**: https://climatedata.imf.org/pages/climate-and-weather#cc1

- **Citation**: International Monetary Fund. 2022. Climate Change Indicators Dashboard. Annual Surface Temperature Change, https://climatedata.imf.org/pages/access-data. Accessed on [2024-05-23].


This all work is used for only semester project task at FAU.


## Work Packages:

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Explore Suitable Dataset. [#1][i1]
2. Initial Project Plan Setup. [#2][i2]
3. Data Extraction and Kaggle API Setup. [#3][i3]
4. Data Transformation. [#4][i4]
5. Data Loading. [#5][i5]
6. Create the pipeline.sh file to test the ETL_Pipeline script. [#6][i6]
7. CI Pipeline Setup for the Project. [#7][i7]
8. Final Project Report. [#8][i8]

[i1]: https://github.com/ZeeshanAhmed13/made-template-23432274/issues/5
[i2]: https://github.com/ZeeshanAhmed13/made-template-23432274/issues/6
[i3]: https://github.com/ZeeshanAhmed13/made-template-23432274/issues/7
[i4]: https://github.com/ZeeshanAhmed13/made-template-23432274/issues/8
[i5]: https://github.com/ZeeshanAhmed13/made-template-23432274/issues/9
[i6]: https://github.com/ZeeshanAhmed13/made-template-23432274/issues/10
[i7]: https://github.com/ZeeshanAhmed13/made-template-23432274/issues/11
[i8]: https://github.com/ZeeshanAhmed13/made-template-23432274/issues/12

