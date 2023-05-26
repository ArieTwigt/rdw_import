# open the required modules
import json

selected_brands = input("Insert the brands for the config file.\nSeperate by ' ':\n")

brands_list = selected_brands.split(" ")

config_dict = {}
config_dict['brands'] = brands_list

config_str = json.dumps(config_dict)

# export to json file
with open("config.json", "w") as file:
    file.write(config_str)


pass