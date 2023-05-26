import os
import pandas as pd
import uuid
from datetime import datetime


# check if the 'data' folder alreay exists
def export_to_csv(selected_value: str, cars_df: pd.DataFrame, export_type:str) -> None:
    '''
    Function for exporting the cars data to a csv-file

    Parameters:
    * selected brand
    * cards_df

    Output:
    * None: File will be written to folder
    
    '''
    # conditional statement to determine the name of the sub-folder
    if export_type == "plate":
        sub_folder_name = "plate"
    elif export_type == "brand":
        sub_folder_name = "brand"
    else:
        sub_folder_name = "other"

    # check if the folder for the car brand already exists
    value_folder_path = f"data/{sub_folder_name}/{selected_value}"

    if not os.path.exists(value_folder_path):
        print(f"Creating folder for {selected_value}")
        os.makedirs(value_folder_path)

    # create our filepath
    new_uuid = uuid.uuid4()
    timestamp = datetime.strftime(datetime.now(), "%Y%m%d%H%M%f")
    file_path = f"{value_folder_path}/{selected_value}_{timestamp}_{new_uuid}.csv"

    cars_df.to_csv(file_path, sep=";", index=False)

    #print(f"✅ Succesfully exported file {file_path}")