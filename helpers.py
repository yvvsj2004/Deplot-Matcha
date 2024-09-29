import csv
import os
import pandas as pd
import re

def get_lineartable_matcha(path,table)->str:
    '''
        Argumets :
        path : str/os.path.join->instance : path to the directory containing table
        table : str : name of the table
        return : str : linearized table 
    '''
    with open(os.path.join(path,table),'r') as cs:
        read_csv = csv.reader(cs)
        list_table = list(read_csv)
    lin_table = ""
    for row in list_table:
        lin_list = " | ".join(l for l in row)
        lin_list += "<0x0A>"
        lin_table += lin_list
    return lin_table


def create_metadata(table_path,dest_path,table_list=None,filename="metadata.csv")->None:
    """
        Argumets :
        table_path : str/os.path.join->instance : path to dir containing tables
        dest_path : str/os.path.join->instance : destination path for metadata file (Image folder)
        table_list : list : list of tables u want to include in metadata file. by default everything in folder will be included
        filename : str : name of the metadata file
        return : None : Creates metadata file in the dest_path
    """
    if table_list is None:
        table_list = os.listdir(table_path)
    with open(os.path.join(dest_path,filename),mode="w",newline='') as meta:
        writer = csv.writer(meta)
        writer.writerow(["file_name","text"])
        for table in (table_list):
            lin_table = get_lineartable_matcha(table_path,table)
            writer.writerow([f"{os.path.splitext(table)[0]}.png",lin_table])



def model_output(model_out,image_list,logfile = "model_out.txt")->None:
    """
        Argumets :
        model_out : list : List containing the outputs of model
        image_list : list : list of charts for which the output is produced (note : In same order/sequence )
        logfile : str : To visualize the actual model output without truncating and padding
        retutn : None :
    """
    with open(logfile,"w") as f:
        print("New output : \n",file=f)
    with open(logfile,"a") as f:
        for out,image  in zip(model_out,image_list):
            print(f"Image : {image}",file=f)
            lines = re.split("<0x0A>",out)
            for line in lines:
                print(line,file=f) 
            print("\n",file=f)   
    return

