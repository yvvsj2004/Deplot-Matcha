import pandas as pd
import re
import os

def matcha_to_df(inp_list,image_list):
    os.makedirs("Output",exist_ok=True)
    for inp,image_name in zip(inp_list,image_list):
        lines = re.split("<0x0A>",inp)

        headers = re.split(' \| ',lines[0])
        headers = [header.strip() for header in headers]
        data=[]
        for line in lines[1:]:
            metrics = re.split(' \| ',line)
            metrics = [metric.strip() for metric in metrics]
            data.append(metrics)

        df = pd.DataFrame(data,columns=headers)
        df.to_csv(os.path.join('Output',f"{os.path.splitext(image_name)[0]}.csv"),index=False)
    return

