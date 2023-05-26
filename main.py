from custom_modules.import_functions import import_cars_by_brand, import_cars_by_plate
from custom_modules.conversion_functions import convert_to_df
from custom_modules.export_functions import export_to_csv

from tqdm import tqdm


if __name__ == "__main__":
    # specify if you want to import by brand or by license plate
    import_type = input("Do you want to import by brand or plate? [brand/plate]\n") or "plate"

    # execute based on import type
    if import_type == "plate":
        # specify the license plate
        selected_plate = input("Insert the license plate, without dashes '-':\n")
        
        # import the data from the api
        car_data = import_cars_by_plate(selected_plate)

        # convert into a data frame
        car_df = convert_to_df(car_data)

        # export data
        export_to_csv(selected_value=selected_plate,
                      cars_df=car_df, 
                      export_type=import_type)
        
        print("🏁 Finished")
    else:
        # provide input for a car brand
        selected_brands = input("🚗 Insert car brands:\n").lower().strip()

        # create a list of brands
        selected_brands_list = selected_brands.split(" ")

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