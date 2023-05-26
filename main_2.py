from custom_modules.import_functions import import_cars_by_brand, import_cars_by_plate
from custom_modules.conversion_functions import convert_to_df
from custom_modules.export_functions import export_to_csv

import json
import sys

from tqdm import tqdm


if __name__ == "__main__":
    # input for import type
    import_type = input("Select input type [plate/brand]:\n") or "brand"

    # based on import_type, execute the functions
    if import_type == "plate":
        selected_plate = input("Insert plate to import:\n")

        # import by plate
        car_data = import_cars_by_plate(selected_plate)

        # convert to pandas DataFrame
        car_df = convert_to_df(car_data)

        # export to csv
        export_to_csv(selected_plate, car_df, export_type=import_type)
        
        print("🏁 Finished")
    elif import_type == "brand":
        # provide input for a car brand
        selection_method = input("Specify brands by input or config [input/config]") or "config"

        if selection_method == "input":
            selected_brands = input("🚗 Insert car brands:\n").lower().strip()

            # create a list of brands
            selected_brands_list = selected_brands.split(" ")
        elif selection_method == "config":
            # open the config file
            with open("config.json", "r") as file:
                config_str = file.read()
            
            # parse the config file
            config_dict = json.loads(config_str)

            # specify the list of brands
            selected_brands_list = config_dict['brands']
        else:
            print("Please select 'input' or 'config'")
            sys.exit()

        # loop
        for selected_brand in tqdm(selected_brands_list, colour="red"):
            print(f"\nImporting {selected_brand}")
            # import the cars
            cars_data = import_cars_by_brand(selected_brand)

            # convert the cars_data list to a pandas DataFrame
            cars_df = convert_to_df(cars_data)

            # export the data to csv
            export_to_csv(selected_brand, cars_df, export_type=import_type)

            print("🏁 Finished")
    else:
        print("Please choose between 'brand' or 'plate'")