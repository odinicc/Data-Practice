import glob                         # this module helps in selecting files
import pandas as pd                 # this module helps in processing CSV files
import xml.etree.ElementTree as ET  # this module helps in processing XML files.
from datetime import datetime
import os
import pathlib


def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process,lines=True)
    return dataframe

def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        dataframe = dataframe.append({"name":name, "height":height, "weight":weight}, ignore_index=True)
    return dataframe

def extract_from_xml_cars(file_to_process):
    dataframe = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price" , "fuel"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for car in root:
        car_model = car.find("car_model").text
        year_of_manufacture = int(car.find("year_of_manufacture").text)
        price = float(car.find("price").text)
        fuel = str(car.find("fuel").text)
        dataframe = dataframe.append({"car_model":car_model, "year_of_manufacture":year_of_manufacture,
                                      "price":price , "fuel":fuel}, ignore_index=True)
    return dataframe


def extract():
    extracted_data = pd.DataFrame(
        columns=['name', 'height', 'weight'])  # create an empty data frame to hold extracted data

    # process all csv files
    for csvfile in glob.glob("*.csv"):
        extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)

    # process all json files
    for jsonfile in glob.glob("*.json"):
        extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)

    # process all xml files
    for xmlfile in glob.glob("*.xml"):
        extracted_data = extracted_data.append(extract_from_xml(xmlfile), ignore_index=True)
    return extracted_data

def extract_cars():
    log("Extract Cars Job Started")
    # create an empty data frame to hold extracted data
    extracted_data = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price','fuel'])

    # process all csv files
    path =  os.path.join(os.getcwd(), "dealership_data")

    for file in os.listdir(path):
        if file.endswith(".csv"):
            file_path = os.path.join(path, file)
            extracted_data = extracted_data.append(extract_from_csv(file_path), ignore_index=True)
        elif file.endswith(".json"):
            file_path = os.path.join(path, file)
            extracted_data = extracted_data.append(extract_from_json(file_path), ignore_index=True)
        elif file.endswith(".xml"):
            file_path = os.path.join(path, file)
            extracted_data = extracted_data.append(extract_from_xml_cars(file_path), ignore_index=True)
    log("Extract Cars Job phase Ended")
    return extracted_data



def transform(data):
    log("Transform phase Started")
        # Round the price columns to 2 decimal
    data['price'] = round(data.price, 2)

    log("Transform phase Ended")
    return data

def load(targetfile, data_to_load):
    log("Load phase Started")
    data_to_load.to_csv(targetfile)
    log("Load phase Ended")

def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    print("Log message: ",message)
    with open("logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')


tmpfile    = "dealership_temp.tmp"               # file used to store all extracted data
logfile    = "dealership_logfile.txt"            # all event logs will be stored in this file
targetfile = "dealership_transformed_data.csv"   # file where transformed data is stored

extracted_data = extract_cars()
transformed_data = transform(extracted_data)
load(targetfile,transformed_data)

#log("ETL Job Ended")


