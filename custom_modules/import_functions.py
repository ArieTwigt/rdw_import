# import requirded modules
import requests
from typing import List

# specify endpoint
def import_cars_by_brand(brand:str, allow_empty:bool=False) -> List:
    '''
    Function to download a list of cars for a given brand

    '''
    # uppercase the brand
    brand_upper = brand.upper()

    # compose the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # get the data from the request
    data = response.json()

    # evaluate if the data is not empty
    if len(data) == 0:
        print(f"No cars returned for {brand}")

        if not allow_empty:
            raise ValueError(f"❌ The value for brand '{brand}' did not return any cars")

    return data


def import_cars_by_plate(plate:str, allow_empty:bool=False) -> List:
    '''
    Function to download a list of cars for a given brand

    '''
    # uppercase the brand
    plate_upper = plate.upper()

    # compose the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={plate_upper}"

    # execute the request
    response = requests.get(endpoint)

    # get the data from the request
    data = response.json()

    # evaluate if the data is not empty
    if len(data) == 0:
        print(f"No cars returned for {plate}")

        if not allow_empty:
            raise ValueError(f"❌ The value for brand '{plate}' did not return any cars")

    return data