# SRA_for_CDC_v2
## Introduction
Pipeline for download SRA file from NCBI SRA database and do assembly with shovill (https://github.com/tseemann/shovill).
## Main Step
### Step1: prepareing data
1. A csv file with all NCBI Run_ID which you want to downlaod. The column name shoud be 'Run'.
2. touch a log which is going to record the assebmly situation of each runs.
### Step2: Run SRA_assembly.py
Required arguments:
1. --runs RUNS : input your csv file.
2. --sra_dir SRA_DIR : creat a temp_folder to save sra files.
