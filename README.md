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
4. --output OUTPUT - Create a folder to save all contigs.fa after assembly of all sra files.
5. --n N - Numbers of download sra files from NCBI in one times.
After a run finised asseemly, you can see contigs.fa after assembly in output file as [Run_id]_contig.fa.
### Step3: Run SRA_assembly.py again if the network is shutdown or connect to NCBI is too slow.
1. The log file you create will record which run is assembled completed or have other situations, for example: 'Run SRR00000 is ok.'
2. When you run this SRA_assembly.py again and input the same log file, it will skip the runs which already finished in last time.
### Step4: Create a new table that remove the finished run with log file by RmRunInLog.py.
1. 

