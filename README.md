# MS Azure Machine Learning Many Models #1

**Project**: Selecting the Optimal Machine Learning Model for Time Series Forecasting (Step 1: Generating a data source on a cluster of virtual machines)

**Consumer**: Personal Project

**Program languages**: Python, Azure CLI v2

**Python libraries are used**: pandas, pyarrow, mltable, azureml-core, azureml-dataset-runtime

**Description**: The first phase of the project involves generating a data source containing hundreds of thousands of time series. The generation is performed using a specified algorithm written in Python, which uses a CSV file containing the source data for each time series as its input. Since the data array is generated independently for each source record, this allows the process to be parallelized and a cluster of virtual machines to be used. 

The project file structure:

many-models-data-generation
 - data
    - base_seed.csv - base seed CSV
    - MLTable - data asset description for mini-batches partitioning
 - environment
    - conda_env.yml - parallel job dependencies
 - src
    - entry_script.py - data generation script
 - data_asset_seed.yml - Data Asset description for registration
 - generation_job.yml - parallel job description

**Results / Key Findings:** A cluster of 4 dedicated Standard_F2s_v2 (2 cores, 4 GB RAM, 16 GB disk) virtual machines was used to solve this task. The resulting Parquet dataset, stored in a BLOB storage, contains ~10⁷ records. 

**Illustrations**: Job Iterations, Dataset Size

![alt text](https://github.com/dmitrii-govorukhin/MS_Azure_Machine_Learning_Many_Models/blob/main/Job_Iterations.png?raw=true)

![alt text](https://github.com/dmitrii-govorukhin/MS_Azure_Machine_Learning_Many_Models/blob/main/Dataset_size.png?raw=true)
