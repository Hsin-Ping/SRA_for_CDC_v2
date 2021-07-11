# SRA_for_CDC_v2
## Introduction
Pipeline for download SRA file from NCBI SRA database and do assembly with shovill (https://github.com/tseemann/shovill).
## Main Step
### Step1: prepareing data
1. A csv file with all NCBI Run_ID which you want to downlaod. The column name shoud be 'Run'.
2. touch a log which is going to record the assebmly situation of each runs.
### Step2: Run SRA_assembly.py
usage: Download avaliable runs from NCBI sra database and do assembly. 
[-h] --runs RUNS\n
     --sra_dir SRA_DIR\n 
     --log LOG 
     --output OUTPUT
     [--assembly_dir ASSEMBLY_DIR]
     [--tmpdir TMPDIR]
     [--gsize GSIZE]
     [--threads THREADS]
     [--n N]                                                  

optional arguments:
  -h, --help            show this help message and exit
  --runs RUNS           Big runinfo table of runs need to assembly.
  --sra_dir SRA_DIR     Temp folder to save runs.
  --log LOG             The file to recored runs which finished assembly each
                        time.
  --output OUTPUT       Folder to save Contigs.fa after assembly of eah runs.
  --assembly_dir ASSEMBLY_DIR
                        Temp folder to save assembly.
  --tmpdir TMPDIR       Directory of temp folder default: '/tmp'
  --gsize GSIZE         Estimated genome size(MB) eg. 3.2M. default: ''
  --threads THREADS     Number of threads to use. default: 8
  --n N                 count of download sra file eahc time
