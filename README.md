# SRA_for_CDC_v2
## Introduction
Pipeline for download SRA file from NCBI SRA database and do assembly with shovill (https://github.com/tseemann/shovill).
## Main Step
### Step1: Data preparing
1. A csv file with all NCBI Run_ID which you want to downlaod. The column name shoud be 'Run'.
2. touch a log which is going to record the assebmly situation of each runs.
### Step2: Run SRA_assembly.py
Required arguments:
1. --runs RUNS - Input your csv file.
2. --sra_dir SRA_DIR - Creat a temp_folder to save sra files.
3. --log Log - Input your log file.
4. --output - Create a folder to save all contigs.fa after assembly of all sra files.
5. --n N - Numbers of download sra files from NCBI in one times.
 
