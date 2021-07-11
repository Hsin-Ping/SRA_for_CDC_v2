import pandas as pd
import argparse



def main():
    parser = argparse.ArgumentParser("Creat a new table with un-downloaded runs for running SRA_assembly.py next time.")
    parser.add_argument("--table",required = True, help = "Input table in SRA_assembly.py.")
    parser.add_argument("--log",required = True, help = "Today's log file.")
    args = parser.parse_args()
    
    table = args.table
    log = args.log
   
    df = pd.read_csv(table)
    df_run = list(df['Run'])
    df = df.set_index(['Run'])
    f = open(log,"r")
    log_file = f.read().split("\n")
    run_lines = list(filter(lambda x:len(x.split(" "))>=4,log_file))
    log_run = list(map(lambda x : x.split(" ")[1],run_lines))
    run_id = list(filter(lambda x : x in log_run,df_run))
    df2 = df.drop(run_id,axis = 0)
    df2.to_csv("m_run_table.csv")
    print("Total",len(df2),"remains need to assembly. Next time start wiht run",df2.index[0],".")


if __name__ == '__main__':
    main()
